from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pandas import DataFrame

from .database import DatabasePyKx
from .database_rest import DatabaseRest
from .kdbai_exception import KDBAIException
from .session import SessionPyKx
from .session_rest import SessionRest
from .table import TablePyKx
from .table_rest import TableRest


KDBAI_CLOUD = 'https://cloud.kdb.ai'
MODE_QIPC = 'qipc'
MODE_REST = 'rest'

class Session:
    """Session class to maintain connection to KDB.AI server"""

    def __init__(
            self,
            api_key: Optional[str] = None,
            *,
            endpoint: Optional[str] = 'http://localhost:8082',
            host: Optional[str] = None,
            port: Optional[int] = None,
            mode: Optional[str] = None,
            options: Optional[dict] = None) -> None:
        """Create a connection to a KDB.AI server.

        Args:
            api_key: API Key to be used for authentication.
            endpoint: REST server endpoint to connect to.
            host: QIPC host to connect to (defaults to endpoint's hostname).
            port: QIPC port to connect to (defaults to endpoint's port).
            mode: Communication mode betwwen client and server. [qipc|rest]
            options: Extra parameters to create connection.

        Example:
            Open a session on KDB.AI Cloud with an api key:

            ```python
            session = Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY', mode='rest')
            ```

            Open a session on a custom KDB.AI instance on http://localhost:8082:

            ```python
            session = Session(endpoint='http://localhost:8082', mode='qipc')
            ```

            Alternatively you can create a session with `host` and `port` parameters:
            ```python
            session = Session(host='localhost', port=8082, endpoint=None, mode='qipc')
            ```
        """
        if mode is None:
            if endpoint is not None and endpoint.startswith(KDBAI_CLOUD):
                mode = MODE_REST
            else:
                mode = MODE_QIPC

        if mode == MODE_REST:
            self._session = SessionRest(api_key=api_key, endpoint=endpoint)
        elif mode == MODE_QIPC:
            self._session = SessionPyKx(api_key=api_key,
                                        endpoint=endpoint,
                                        host=host,
                                        port=port,
                                        options=options or dict())
        else:
            raise KDBAIException(f'Unsupported mode: {mode}')

    def close(self) -> None:
        """Close connection to the server"""
        return self._session.close()

    def version(self) -> dict:
        """Retrieve version information from server"""
        return self._session.version()

    def create_database(self, database: str) -> Database:
        """Create a new database

        Args:
            database: name of the database to be created.

        Returns:
            A Database object.

        Examples:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.create_database('my_new_database')
            ```

        Raises:
            KDBAIException: Raised when an error occurs during creating the database.
        """
        return Database(self._session.create_database(database))

    def databases(self, include_tables: bool = False) -> List[Database]:
        """List exising databases in current session.

        Args:
            include_tables: if True, the table info in each database will also be fetched one by one.
                            if False, only names of the databases will be set on the Database objects.

        Returns:
            A list of Database objects.

        Examples:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                databases = session.databases(include_tables: True)
            ```

        Raises:
            KDBAIException: Raised when an error occurs during retrieving database info.
        """
        return [Database(db) for db in self._session.databases(include_tables)]

    def database(self, database: str) -> Database:
        """Fetch info of a database in session.

        Args:
            database: name of the database to fetch.

        Returns:
            A Database object.

        Examples:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
            ```

        Raises:
            KDBAIException: Raised when an error occurs during retrieving database info.
        """
        return Database(self._session.database(database))


class Database:
    """Database class to handle database level operations"""

    def __init__(self, database: Union[DatabasePyKx, DatabaseRest]) -> None:
        self._database = database

    def __str__(self) -> str:
        return f'KDBAI database "{self._database.name}"'

    def __repr__(self) -> str:
        return str(self)

    def refresh(self) -> None:
        """Refresh database"""
        return self._database.refresh()

    def create_table(self,
                     table: str,
                     schema: Optional[List[Dict[str, Any]]] = None,
                     indexes: List[Dict[str, Any]] = [],
                     partition_column: Optional[str] = None,
                     embedding_configurations: Optional[Dict[str, Any]] = None,
                     external_data_references: Optional[List[Dict[str, Any]]] = None,
                     default_result_type: str = 'pd') -> Table:
        """Create a table with a schema

        Args:
            table: Name of the table to create.
            schema: list of dictionaries containing column name and type
            indexes: list of dictionaries containing index definitions (multiple indexes can be created for each column)
            partition_column: column name if table is partitioned
            embedding_configurations: dictionary containing TSC configurations
            external_data_references: reference info of existing table
            default_result_type: default result type for search and query methods (pd|py|q)

        Returns:
            A newly created `Table` object based on parameters.

        Raises:
            KDBAIException: Raised when a error happens during the creation of the table.

        Example Flat/qFlat Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index = {'name': 'flat_index', 'column': 'embeddings', 'type': 'flat',
                     'params': {'dims': 25, 'metric': 'L2'}}
            table = session.create_table('documents', schema=schema, indexes=[index])
            ```

        Example IVF Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index = {'name': 'ivf_index', 'column': 'embeddings', 'type': 'ivf',
                     'params': {'metric': 'L2', 'nclusters': 8}}
            table = session.create_table('documents', schema=schema, indexes=[index])
            ```

        Example IVFPQ Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index = {{'name': 'ivf_index', 'column': 'embeddings', 'type': 'ivfpq',
                      'params': {'metric': 'L2', 'nclusters': 8, 'nbits': 8, 'nsplits': 5}}
            table = session.create_table('documents', schema=schema, indexes=[index])
            ```

        Example HNSW Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index = {'name': 'hnsw_index', 'column': 'embeddings', 'type': 'hnsw',
                     'params': {'dims': 25, 'metric': 'L2', 'M': 8, 'efConstruction': 8}}
            table = session.create_table('documents', schema=schema, indexes=[index])
            ```

        Example Sparse Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index = {'name': 'sparse_index', 'column': 'sparse_col', 'type': 'bm25',
                     'params': {'k': 1.25, 'b': 0.75}}
            table = session.create_table('documents', schema=schema, indexes=[index])
            ```

        Example Flat with Sparse Index:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'},
                {'name': 'sparse_col', 'type': 'general'}
            ]
            index_flat = {'name': 'flat_index', 'column': 'embeddings', 'type': 'flat',
                          'params': {'dims': 25, 'metric': 'L2'}}
            index_sparse = {'name': 'sparse_index', 'column': 'sparse_col', 'type': 'bm25',
                            'params': {'k': 1.25, 'b': 0.75}}
            table = session.create_table('documents', schema=schema, indexes=[index_flat, index_sparse])
            ```

        Examle Flat with TSC:
            ```python
            schema = [
                {'name': 'id', 'type': 'int32'},
                {'name': 'embeddings', 'type': 'float32s'}
            ]
            index_flat = {'name': 'flat_index', 'column': 'embeddings', 'type': 'flat',
                          'params': {'dims': 25, 'metric': 'L2'}}
            embedding_conf = {'embeddings': {"dims": 4, "type": "tsc", "on_insert_error": "reject_all" }}
            table = session.create_table('documents',
                                         schema=schema,
                                         indexes=[index_flat],
                                         embedding_configurations=embedding_conf)
            ```
        """
        return Table(self._database.create_table(table,
                                                 schema,
                                                 indexes,
                                                 partition_column,
                                                 embedding_configurations,
                                                 external_data_references,
                                                 default_result_type))

    def drop(self) -> bool:
        """Delete database

        Returns:
            True if drop is successful, raises exception otherwise.

        Example:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
                database.drop()
            ```

        Raises:
            KDBAIException: Raised when an error occurs during deleting the database.
        """
        return self._database.drop()

    def table(self, table: str) -> Table:
        """Retrieve an existing table from server. Table metadata is updated.

        Args:
            table: Name of the table to retrieve.

        Returns:
                A `Table` object representing the KDB.AI table.

        Example:
            Retrieve the `trade` table:

            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
                table = database.table('trade')
            ```

        Raises:
            KDBAIException: Raised when an error occurs during retrieving the table.
        """
        return Table(self._database.table(table))

    @property
    def name(self) -> str:
        """Access to database name"""
        return self._database.name

    @property
    def tables(self) -> List[Table]:
        """Access to list of tables that already exist in the database.

        Returns:
                A list of `Table` objects.

        Example:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
                tables = database.tables

                database.refresh()  # update table info for database
                tables = database.tables
            ```
        """
        return [Table(t) for t in self._database.tables]


class Table:
    """Table class to handle table level operations"""

    def __init__(self, table: Union[TablePyKx, TableRest]) -> None:
        self._table = table

    def __str__(self) -> str:
        return f'KDBAI table "{self._table.name}"'

    def __repr__(self) -> str:
        return str(self)

    def refresh(self):
        """Refresh table meta information

        Example:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
                table = database.table('trade')

                # background operations that may affect table metadata
                table.refresh()  # table info is updated
            ```
        """
        return self._table.refresh()

    def index(self, name: str) -> Dict[str, Any]:
        """Return information about a specific index.

        Example:
            ```python
                session = kdbai.Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
                database = session.database('my_database')
                table = database.table('trade')
                print(table.index('my_hnsw_index'))
            ```
        """
        return self._table.index(name)

    def train(self, payload: DataFrame) -> bool:
        """Train the index (IVF and IVFPQ only).

        Args:
            payload (DataFrame): Pandas dataframe with column names/types matching the target table.

        Returns:
            True if training was succesful, raises exception otherwise.

        Examples:
            ```python
            from datetime import timedelta
            from datetime import datetime

            ROWS = 50
            DIMS = 10

            data = {
                "time": [timedelta(microseconds=np.random.randint(0, int(1e10))) for _ in range(ROWS)],
                "sym": [f"sym_{np.random.randint(0, 999)}" for _ in range(ROWS)],
                "realTime": [datetime.utcnow() for _ in range(ROWS)],
                "price": [np.random.rand(DIMS).astype(np.float32) for _ in range(ROWS)],
                "size": [np.random.randint(1, 100) for _ in range(ROWS)],
            }
            df = pd.DataFrame(data)
            table.train(df)
            ```

        Raises:
            KDBAIException: Raised when an error occurs during training.
        """
        return self._table.train(payload)

    def insert(self, payload: DataFrame) -> Dict[str, Any]:
        """Insert data into the table.

        Args:
            payload (DataFrame): Pandas dataframe with column names/types matching the target table.

        Returns:
            A dict which contains information about the inserted rows.

        Examples:
            ```python
            ROWS = 50
            DIMS = 10

            data = {
                "time": [timedelta(microseconds=np.random.randint(0, int(1e10))) for _ in range(ROWS)],
                "sym": [f"sym_{np.random.randint(0, 999)}" for _ in range(ROWS)],
                "realTime": [datetime.utcnow() for _ in range(ROWS)],
                "price": [np.random.rand(DIMS).astype(np.float32) for _ in range(ROWS)],
                "size": [np.random.randint(1, 100) for _ in range(ROWS)],
            }
            df = pd.DataFrame(data)
            table.insert(df)
            ```

        Raises:
            KDBAIException: Raised when an error occurs during insert.
        """
        return self._table.insert(payload)

    def query(self,
              *,
              filter: Optional[List[List[Any]]] = None,
              sort_columns: Optional[List[str]] = None,
              group_by: Optional[List[str]] = None,
              aggs: Optional[Dict[str, Any]] = None,
              limit: Optional[int] = None,
              result_type: Optional[str] = None):
        """Query data from the table.

        Args:
            filter: A list of filter conditions as triplets in the following format:
                `[['function', 'column name', 'parameter'], ... ]`
                See all filter operators [here](https://code.kx.com/kdbai/use/filter.html#supported-filter-functions)
            sort_columns: List of column names to sort on.
            group_by: A list of column names to use for group by.
            aggs: Dictionary specifying aggregation/projection on table.
                If we want to return subset of columns, specify column name as key and values.
                If we want to aggregate a column, key must be target column name and value mmust be agg function
                and source column
                See all aggregation functions [here](https://code.kx.com/kdbai/use/query.html#supported-aggregations)
            limit: Specify maximum number of rows returned.
            result_type: data type to convert result into (pd|py|q)

        Returns:
            Table with the query results.

        Examples:
            ```python
            table.query(group_by = ['sensorID', 'qual'])
            table.query(filter = [['within', 'qual', [0, 2]]])

            # Select subset of columns
            aggs = dict()
            aggs['sensorID'] = 'sensorID'  # include this column in result
            aggs['cost'] = 'price'  # rename price column to cost
            table.query(aggs=aggs)

            aggs = {'maxPrice': ['max', 'price']}  # get max price
            table.query(aggs=aggs)
            ```

        Raises:
            KDBAIException: Raised when an error occurs during query.
        """
        return self._table.query(filter=filter,
                                 sort_columns=sort_columns,
                                 group_by=group_by,
                                 aggs=aggs,
                                 limit=limit,
                                 result_type=result_type)

    def search(self,
               vectors: Dict[str, Any],
               n: int = 1,
               *,
               type: Optional[str] = None,
               index_params: Optional[Dict[str, Any]] = None,
               options: Optional[Dict[str, Any]] = None,
               filter: Optional[List[List[Any]]] = None,
               sort_columns: Optional[List[str]] = None,
               group_by: Optional[List[str]] = None,
               aggs: Optional[Dict[str, Any]] = None,
               result_type: Optional[str] = None):
        """Perform similarity search on the table, supports dense or sparse queries.

        Args:
            vectors: Query vectors for the search. Dictionary keys must be index names or column name(tss) to execute
                the search on. Values must be list of vectors containing the search vectors
            n: Number of neighbours to return.
            type: Override basic similarity search type.
            index_params: Index specific options for similarity search.
            options: Additional options for search, e.g: renaming distance column.
            filter: A list of filter conditions as triplets in the following format:
                `[['function', 'column name', 'parameter'], ... ]`
                See all filter operators [here](https://code.kx.com/kdbai/use/filter.html#supported-filter-functions)
            sort_columns: List of column names to sort on.
            group_by: A list of column names to use for group by.
            aggs: Dictionary specifying aggregation/projection on table.
                If we want to return subset of columns, specify column name as key and values.
                If we want to aggregate a column, key must be target column name and value mmust be agg function
                and source column
                See all aggregation functions [here](https://code.kx.com/kdbai/use/query.html#supported-aggregations)
            result_type: data type to convert result into (pd|py|q)

        Returns:
            List tables with one table of matching neighbors for each query vector.

        Examples:
            ```python
            #Find the closest neighbour of a single (dense) query vector
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0]]}, n=1)

            #Find the closest neighbour of a single (sparse) query vector
            table.search(vectors={'my_sparse_index':[{101:1,4578:1,102:1}]}, n=1)

            #Find the 3 closest neighbours of 2 query vectors
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]}, n=3)

            # With aggregation and sorting
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]},
            n=3,
            aggs={'sumSize': ['sum','size']},
            group_by=['sym'],
            sort_by=['sumSize'])

            # Returns a subset of columns for each match
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]}, n=3,
                         aggs={'size': 'size'})
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]}, n=3,
                         aggs={'size': 'size', 'price': 'price'})

            # Filter
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]},
            n=3,
            filter=[['within','size',(5,999)],['like','sym','AAP*']])

            # Customized distance name
            table.search(vectors={'my_index': [[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]]},
            n=3,
            options={"distanceColumn" 'myDist'})

            # Index options
            table.search(vectors=[[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]], n=3, index_params=dict(efSearch=512))
            table.search(vectors=[[0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1]], n=3, index_params=dict(clusters=16))
            ```

        Raises:
            KDBAIException: Raised when an error occurs during search.
        """
        return self._table.search(vectors=vectors,
                                  n=n,
                                  type=type,
                                  index_params=index_params,
                                  options=options,
                                  filter=filter,
                                  sort_columns=sort_columns,
                                  group_by=group_by,
                                  aggs=aggs,
                                  result_type=result_type)

    def drop(self) -> None:
        """Drop the table.

        Examples:
            ```python
            table.drop()
            ```

        Raises:
            KDBAIException: Raised when an error occurs during the table deletion.
        """
        return self._table.drop()

    def update_indexes(self, indexes: List[str], parts: Optional[List[Any]] = None) -> bool:
        """Updates indexes

        Args:
            indexes: list of index names to update.
            parts: list of partition values to update. If None, all partittions are updated.

        Examples:
            ```python
            table.update_indexes(indexes=['hnsw_accurate', 'my_sparse_index'])
            table.update_indexes(indexes=['hnsw_fast'], parts=['AAML', 'WDEF'])
            ```

        Raises:
            KDBAIException: Raised when an error occurs during updating the indexes.
        """
        return self._table.update_indexes(indexes, parts)

    @property
    def name(self) -> str:
        """Table name"""
        return self._table.name

    @property
    def schema(self) -> List[dict]:
        """Table schema"""
        return self._table.schema

    @property
    def indexes(self) -> List[dict]:
        """Indexes specified on table"""
        return self._table.indexes

    @property
    def default_result_type(self) -> str:
        """Default table type used for search and query"""
        return self._table.default_result_type

    @default_result_type.setter
    def default_result_type(self, value):
        self._table.default_result_type = value

    def __eq__(self, rhs: Table) -> bool:
        if not isinstance(rhs, Table):
            return False
        return self._table == rhs._table

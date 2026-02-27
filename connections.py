from typing import Optional
from snowflake.snowpark.session import Session
from settings import Settings


class SnowflakeConnection:
  _instance = None
  _session: Optional[Session] = None

  _connection_parameters = {
    "account": Settings.ACCOUNT_INDENTIFIER,
    "user": Settings.USER,
    "password": Settings.PASSWORD,
    "role": Settings.ROLE,
    "warehouse": Settings.WAREHOUSE,
    "database": Settings.DATABASE,
    "schema": Settings.SCHEMA,
  }


  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SnowflakeConnection, cls).__new__(cls)
      cls._instance._create_session()
    return cls._instance


  def _create_session(self):
    if self.__class__._session is None:
      try:
        print("Creating new Snowflake session...")
        self.__class__._session = (
          Session.builder
          .configs(self._connection_parameters)
          .create()
        )
      except Exception as e:
        raise RuntimeError(f"Failed to connect to Snowflake: {e}")


  def get_session(self) -> Session:
    if self.__class__._session is None:
      self._create_session()
    return self.__class__._session


  def close(self):
    if self.__class__._session:
      print("Closing Snowflake session...")
      self.__class__._session.close()
      self.__class__._session = None
      self.__class__._instance = None
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.database import Base
from models import email_otp  # make sure this exists

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

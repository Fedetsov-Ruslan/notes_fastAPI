"""1 upgrade

Revision ID: 1be32ab58502
Revises: 186dfa18f3d0
Create Date: 2024-09-15 17:04:36.685143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1be32ab58502'
down_revision: Union[str, None] = '186dfa18f3d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('record', 'auther',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('record_tags_fkey', 'record', type_='foreignkey')
    op.drop_column('record', 'tags')
    op.alter_column('tagsrecord', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('tagsrecord', 'record_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('user', 'registered_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.alter_column('user', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('tagsrecord', 'record_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('tagsrecord', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('record', sa.Column('tags', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('record_tags_fkey', 'record', 'tags', ['tags'], ['id'])
    op.alter_column('record', 'auther',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

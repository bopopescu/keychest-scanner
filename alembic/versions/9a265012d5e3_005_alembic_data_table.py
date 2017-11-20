"""005 alembic data table

Revision ID: 9a265012d5e3
Revises: 9a260012d5e3
Create Date: 2017-07-06 20:31:29.569271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a265012d5e3'
down_revision = '9a260012d5e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alembic_version_data',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('schema_ver', sa.BigInteger(), nullable=True),
    sa.Column('data_ver', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alembic_version_data')
    # ### end Alembic commands ###
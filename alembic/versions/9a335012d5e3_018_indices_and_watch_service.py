"""018 indices and watch service

Revision ID: 9a335012d5e3
Revises: 9a330012d5e3
Create Date: 2017-07-12 14:19:09.244368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a335012d5e3'
down_revision = '9a330012d5e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crtsh_query', sa.Column('service_id', sa.BigInteger(), nullable=True))
    op.create_index(op.f('ix_crtsh_query_service_id'), 'crtsh_query', ['service_id'], unique=False)
    op.create_foreign_key('crtsh_watch_watch_service_id', 'crtsh_query', 'watch_service', ['service_id'], ['id'], ondelete='SET NULL')

    op.add_column('keychest_agent', sa.Column('last_seen_ip', sa.String(length=191), nullable=True))

    op.create_index(op.f('ix_keychest_agent_api_key'), 'keychest_agent', ['api_key'], unique=False)

    op.add_column('watch_service', sa.Column('crtsh_input_id', sa.BigInteger(), nullable=True))
    op.create_index(op.f('ix_watch_service_crtsh_input_id'), 'watch_service', ['crtsh_input_id'], unique=False)
    op.create_unique_constraint(None, 'watch_service', ['service_name'])
    op.create_foreign_key('fk_watch_service_crtsh_input_id', 'watch_service', 'crtsh_input', ['crtsh_input_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_watch_service_crtsh_input_id', 'watch_service', type_='foreignkey')
    op.drop_constraint('service_name', 'watch_service', type_='unique')
    op.drop_index(op.f('ix_watch_service_crtsh_input_id'), table_name='watch_service')
    op.drop_column('watch_service', 'crtsh_input_id')
    op.drop_index(op.f('ix_keychest_agent_api_key'), table_name='keychest_agent')
    op.drop_column('keychest_agent', 'last_seen_ip')
    op.drop_constraint('crtsh_watch_watch_service_id', 'crtsh_query', type_='foreignkey')
    op.drop_index(op.f('ix_crtsh_query_service_id'), table_name='crtsh_query')
    op.drop_column('crtsh_query', 'service_id')
    # ### end Alembic commands ###
"""037 client api

Revision ID: 7fa70183953e
Revises: 8fedecff0ae9
Create Date: 2017-09-15 15:11:24.929351+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7fa70183953e'
down_revision = '8fedecff0ae9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_keys',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=191), nullable=True),
    sa.Column('api_key', sa.String(length=191), nullable=True),
    sa.Column('email_claim', sa.String(length=191), nullable=True),
    sa.Column('ip_registration', sa.String(length=191), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=10, unsigned=True), nullable=True),
    sa.Column('last_seen_active_at', sa.DateTime(), nullable=True),
    sa.Column('last_seen_ip', sa.String(length=191), nullable=True),
    sa.Column('verified_at', sa.DateTime(), nullable=True),
    sa.Column('revoked_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_api_keys_user_users_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_keys_api_key'), 'api_keys', ['api_key'], unique=True)
    op.create_index(op.f('ix_api_keys_email_claim'), 'api_keys', ['email_claim'], unique=False)
    op.create_index(op.f('ix_api_keys_ip_registration'), 'api_keys', ['ip_registration'], unique=False)
    op.create_index(op.f('ix_api_keys_user_id'), 'api_keys', ['user_id'], unique=False)
    op.create_table('api_keys_log',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('api_key_id', sa.BigInteger(), nullable=True),
    sa.Column('req_ip', sa.String(length=191), nullable=True),
    sa.Column('req_email', sa.String(length=191), nullable=True),
    sa.Column('req_challenge', sa.String(length=191), nullable=True),
    sa.Column('action_type', sa.String(length=191), nullable=True),
    sa.Column('action_data', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['api_key_id'], ['api_keys.id'], name='fk_api_keys_log_api_key_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_keys_log_action_type'), 'api_keys_log', ['action_type'], unique=False)
    op.create_index(op.f('ix_api_keys_log_api_key_id'), 'api_keys_log', ['api_key_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_index(op.f('ix_api_keys_log_api_key_id'), table_name='api_keys_log')
    op.drop_index(op.f('ix_api_keys_log_action_type'), table_name='api_keys_log')
    op.drop_table('api_keys_log')
    # op.drop_index(op.f('ix_api_keys_user_id'), table_name='api_keys')
    op.drop_index(op.f('ix_api_keys_ip_registration'), table_name='api_keys')
    op.drop_index(op.f('ix_api_keys_email_claim'), table_name='api_keys')
    op.drop_index(op.f('ix_api_keys_api_key'), table_name='api_keys')
    op.drop_table('api_keys')
    # ### end Alembic commands ###

"""006 refactoring and agents

Revision ID: 9a270012d5e3
Revises: 9a265012d5e3
Create Date: 2017-07-09 17:17:17.300071

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9a270012d5e3'
down_revision = '9a265012d5e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'crtsh_input_base_domain_id', 'crtsh_input', type_='foreignkey')
    op.create_foreign_key('crtsh_input_base_domain_id', 'crtsh_input', 'base_domain', ['sld_id'], ['id'],
                          ondelete='SET NULL')

    op.drop_constraint(u'crtsh_watch_target_id', 'crtsh_query', type_='foreignkey')
    op.drop_constraint(u'crtsh_watch_input_id', 'crtsh_query', type_='foreignkey')
    op.drop_constraint(u'crtsh_watch_sub_target_id', 'crtsh_query', type_='foreignkey')
    op.create_foreign_key('crtsh_watch_sub_target_id', 'crtsh_query', 'subdomain_watch_target', ['sub_watch_id'],
                          ['id'], ondelete='SET NULL')
    op.create_foreign_key('crtsh_watch_target_id', 'crtsh_query', 'watch_target', ['watch_id'], ['id'],
                          ondelete='SET NULL')
    op.create_foreign_key('crtsh_watch_input_id', 'crtsh_query', 'crtsh_input', ['input_id'], ['id'],
                          ondelete='SET NULL')

    op.drop_constraint(u'dns_watch_target_id', 'scan_dns', type_='foreignkey')
    op.create_foreign_key('dns_watch_target_id', 'scan_dns', 'watch_target', ['watch_id'], ['id'], ondelete='SET NULL')

    op.drop_constraint(u'sgap_watch_target_id', 'scan_gaps', type_='foreignkey')
    op.create_foreign_key('sgap_watch_target_id', 'scan_gaps', 'watch_target', ['watch_id'], ['id'], ondelete='CASCADE')

    op.drop_constraint(u'tls_watch_target_id', 'scan_handshakes', type_='foreignkey')
    op.create_foreign_key('tls_watch_target_id', 'scan_handshakes', 'watch_target', ['watch_id'], ['id'],
                          ondelete='SET NULL')

    op.drop_constraint(u'shist_watch_target_id', 'scan_history', type_='foreignkey')
    op.create_foreign_key('shist_watch_target_id', 'scan_history', 'watch_target', ['watch_id'], ['id'],
                          ondelete='CASCADE')

    op.drop_constraint(u'wa_sub_res_watch_target_id', 'subdomain_results', type_='foreignkey')
    op.create_foreign_key('wa_sub_res_watch_target_id', 'subdomain_results', 'subdomain_watch_target', ['watch_id'],
                          ['id'], ondelete='CASCADE')

    op.drop_constraint(u'sub_wt_base_domain_id', 'subdomain_watch_target', type_='foreignkey')
    op.create_foreign_key('sub_wt_base_domain_id', 'subdomain_watch_target', 'base_domain', ['top_domain_id'], ['id'],
                          ondelete='SET NULL')

    op.drop_constraint(u'wa_sub_users_id', 'user_subdomain_watch_target', type_='foreignkey')
    op.drop_constraint(u'wa_sub_watch_target_id', 'user_subdomain_watch_target', type_='foreignkey')
    op.create_foreign_key('wa_sub_watch_target_id', 'user_subdomain_watch_target', 'subdomain_watch_target',
                          ['watch_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('wa_sub_users_id', 'user_subdomain_watch_target', 'users', ['user_id'], ['id'],
                          ondelete='CASCADE')

    op.drop_constraint(u'wa_users_id', 'user_watch_target', type_='foreignkey')
    op.drop_constraint(u'wa_watch_target_id', 'user_watch_target', type_='foreignkey')
    op.create_foreign_key('wa_users_id', 'user_watch_target', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('wa_watch_target_id', 'user_watch_target', 'watch_target', ['watch_id'], ['id'],
                          ondelete='CASCADE')

    op.drop_constraint(u'wt_base_domain_id', 'watch_target', type_='foreignkey')
    op.create_foreign_key('wt_base_domain_id', 'watch_target', 'base_domain', ['top_domain_id'], ['id'],
                          ondelete='SET NULL')

    op.drop_constraint(u'who_base_domain_id', 'whois_result', type_='foreignkey')
    op.create_foreign_key('who_base_domain_id', 'whois_result', 'base_domain', ['domain_id'], ['id'],
                          ondelete='CASCADE')

    op.drop_constraint(u'sjob_crtsh_query_id', 'scan_jobs', type_='foreignkey')
    op.drop_constraint(u'sjob_whois_result_id', 'scan_jobs', type_='foreignkey')
    op.drop_constraint(u'sjob_scan_dns_id', 'scan_jobs', type_='foreignkey')
    op.create_foreign_key('sjob_scan_dns_id', 'scan_jobs', 'scan_dns', ['dns_check_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('sjob_crtsh_query_id', 'scan_jobs', 'crtsh_query', ['crtsh_check_id'], ['id'],
                          ondelete='SET NULL')
    op.create_foreign_key('sjob_whois_result_id', 'scan_jobs', 'whois_result', ['whois_check_id'], ['id'],
                          ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('who_base_domain_id', 'whois_result', type_='foreignkey')
    op.create_foreign_key(u'who_base_domain_id', 'whois_result', 'base_domain', ['domain_id'], ['id'])

    op.drop_constraint('wt_base_domain_id', 'watch_target', type_='foreignkey')
    op.create_foreign_key(u'wt_base_domain_id', 'watch_target', 'base_domain', ['top_domain_id'], ['id'])
    op.drop_constraint('wa_watch_target_id', 'user_watch_target', type_='foreignkey')
    op.drop_constraint('wa_users_id', 'user_watch_target', type_='foreignkey')
    op.create_foreign_key(u'wa_watch_target_id', 'user_watch_target', 'watch_target', ['watch_id'], ['id'])
    op.create_foreign_key(u'wa_users_id', 'user_watch_target', 'users', ['user_id'], ['id'])
    op.drop_constraint('wa_sub_users_id', 'user_subdomain_watch_target', type_='foreignkey')
    op.drop_constraint('wa_sub_watch_target_id', 'user_subdomain_watch_target', type_='foreignkey')
    op.create_foreign_key(u'wa_sub_watch_target_id', 'user_subdomain_watch_target', 'subdomain_watch_target',
                          ['watch_id'], ['id'])
    op.create_foreign_key(u'wa_sub_users_id', 'user_subdomain_watch_target', 'users', ['user_id'], ['id'])
    op.drop_constraint('sub_wt_base_domain_id', 'subdomain_watch_target', type_='foreignkey')
    op.create_foreign_key(u'sub_wt_base_domain_id', 'subdomain_watch_target', 'base_domain', ['top_domain_id'], ['id'])
    op.drop_constraint('wa_sub_res_watch_target_id', 'subdomain_results', type_='foreignkey')
    op.create_foreign_key(u'wa_sub_res_watch_target_id', 'subdomain_results', 'subdomain_watch_target', ['watch_id'],
                          ['id'])
    op.drop_constraint('shist_watch_target_id', 'scan_history', type_='foreignkey')
    op.create_foreign_key(u'shist_watch_target_id', 'scan_history', 'watch_target', ['watch_id'], ['id'])
    op.drop_constraint('tls_watch_target_id', 'scan_handshakes', type_='foreignkey')
    op.create_foreign_key(u'tls_watch_target_id', 'scan_handshakes', 'watch_target', ['watch_id'], ['id'])
    op.drop_constraint('sgap_watch_target_id', 'scan_gaps', type_='foreignkey')
    op.create_foreign_key(u'sgap_watch_target_id', 'scan_gaps', 'watch_target', ['watch_id'], ['id'])
    op.drop_constraint('dns_watch_target_id', 'scan_dns', type_='foreignkey')
    op.create_foreign_key(u'dns_watch_target_id', 'scan_dns', 'watch_target', ['watch_id'], ['id'])
    op.drop_constraint('crtsh_watch_input_id', 'crtsh_query', type_='foreignkey')
    op.drop_constraint('crtsh_watch_target_id', 'crtsh_query', type_='foreignkey')
    op.drop_constraint('crtsh_watch_sub_target_id', 'crtsh_query', type_='foreignkey')
    op.create_foreign_key(u'crtsh_watch_sub_target_id', 'crtsh_query', 'subdomain_watch_target', ['sub_watch_id'],
                          ['id'])
    op.create_foreign_key(u'crtsh_watch_input_id', 'crtsh_query', 'crtsh_input', ['input_id'], ['id'])
    op.create_foreign_key(u'crtsh_watch_target_id', 'crtsh_query', 'watch_target', ['watch_id'], ['id'])
    op.drop_constraint('crtsh_input_base_domain_id', 'crtsh_input', type_='foreignkey')
    op.create_foreign_key(u'crtsh_input_base_domain_id', 'crtsh_input', 'base_domain', ['sld_id'], ['id'])

    op.drop_constraint('sjob_whois_result_id', 'scan_jobs', type_='foreignkey')
    op.drop_constraint('sjob_crtsh_query_id', 'scan_jobs', type_='foreignkey')
    op.drop_constraint('sjob_scan_dns_id', 'scan_jobs', type_='foreignkey')
    op.create_foreign_key(u'sjob_scan_dns_id', 'scan_jobs', 'scan_dns', ['dns_check_id'], ['id'])
    op.create_foreign_key(u'sjob_whois_result_id', 'scan_jobs', 'whois_result', ['whois_check_id'], ['id'])
    op.create_foreign_key(u'sjob_crtsh_query_id', 'scan_jobs', 'crtsh_query', ['crtsh_check_id'], ['id'])
    # ### end Alembic commands ###
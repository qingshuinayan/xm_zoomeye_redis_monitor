"""empty message

Revision ID: 8160d3e0fcf4
Revises: None
Create Date: 2016-10-18 13:25:31.156000

"""

# revision identifiers, used by Alembic.
revision = '8160d3e0fcf4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('RdsInstances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rds_host', sa.String(length=32), nullable=False),
    sa.Column('rds_port', sa.String(length=32), nullable=False),
    sa.Column('add_time', sa.String(length=32), nullable=False),
    sa.Column('rds_pass', sa.String(length=32), nullable=True),
    sa.Column('usermail', sa.String(length=32), nullable=True),
    sa.Column('identify', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_RdsInstances_add_time'), 'RdsInstances', ['add_time'], unique=False)
    op.create_index(op.f('ix_RdsInstances_identify'), 'RdsInstances', ['identify'], unique=True)
    op.create_index(op.f('ix_RdsInstances_rds_host'), 'RdsInstances', ['rds_host'], unique=False)
    op.create_index(op.f('ix_RdsInstances_rds_pass'), 'RdsInstances', ['rds_pass'], unique=False)
    op.create_index(op.f('ix_RdsInstances_rds_port'), 'RdsInstances', ['rds_port'], unique=False)
    op.create_index(op.f('ix_RdsInstances_usermail'), 'RdsInstances', ['usermail'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_RdsInstances_usermail'), table_name='RdsInstances')
    op.drop_index(op.f('ix_RdsInstances_rds_port'), table_name='RdsInstances')
    op.drop_index(op.f('ix_RdsInstances_rds_pass'), table_name='RdsInstances')
    op.drop_index(op.f('ix_RdsInstances_rds_host'), table_name='RdsInstances')
    op.drop_index(op.f('ix_RdsInstances_identify'), table_name='RdsInstances')
    op.drop_index(op.f('ix_RdsInstances_add_time'), table_name='RdsInstances')
    op.drop_table('RdsInstances')
    ### end Alembic commands ###

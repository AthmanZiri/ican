"""empty message

Revision ID: 43bfd9032e66
Revises: None
Create Date: 2014-11-02 14:24:30.424862

"""

# revision identifiers, used by Alembic.
revision = '43bfd9032e66'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('user_role', sa.String(length=15), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('mentor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mentor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_phone', 'users', ['phone'], unique=True)
    op.create_table('universities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('general_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('university_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['university_id'], ['universities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('general_tasks')
    op.drop_table('tasks')
    op.drop_table('universities')
    op.drop_index('ix_users_phone', 'users')
    op.drop_index('ix_users_name', 'users')
    op.drop_index('ix_users_email', 'users')
    op.drop_table('users')
    ### end Alembic commands ###
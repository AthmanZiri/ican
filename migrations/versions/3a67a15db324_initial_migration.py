"""initial migration

Revision ID: 3a67a15db324
Revises: None
Create Date: 2014-10-26 17:16:54.357345

"""

# revision identifiers, used by Alembic.
revision = '3a67a15db324'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_email', 'students', ['email'], unique=True)
    op.create_index('ix_students_name', 'students', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    sa.Column(u'id', sa.INTEGER(), nullable=False),
    sa.Column(u'name', sa.VARCHAR(length=64), nullable=True),
    sa.Column(u'email', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint(u'id')
    )
    op.drop_index('ix_students_name', 'students')
    op.drop_index('ix_students_email', 'students')
    op.drop_table('students')
    ### end Alembic commands ###

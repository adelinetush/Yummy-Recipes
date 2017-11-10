"""empty message

Revision ID: 987f479ed418
Revises: 
Create Date: 2017-11-06 22:36:33.022942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987f479ed418'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_email'), 'User', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_User_email'), table_name='User')
    op.drop_table('User')
    op.drop_table('Recipe')
    op.drop_table('Category')
    # ### end Alembic commands ###
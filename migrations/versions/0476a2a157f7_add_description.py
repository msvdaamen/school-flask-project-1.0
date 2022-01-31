"""Add description

Revision ID: 0476a2a157f7
Revises: 7344d50630dc
Create Date: 2022-01-24 14:15:22.057823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0476a2a157f7'
down_revision = '7344d50630dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'description')
    # ### end Alembic commands ###
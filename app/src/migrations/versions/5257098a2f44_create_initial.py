"""create initial

Revision ID: 5257098a2f44
Revises: 
Create Date: 2023-04-05 19:52:00.985187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5257098a2f44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    # ### end Alembic commands ###

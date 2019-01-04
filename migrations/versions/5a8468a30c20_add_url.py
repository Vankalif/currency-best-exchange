"""add url

Revision ID: 5a8468a30c20
Revises: f20461bc808d
Create Date: 2019-01-04 18:18:26.374363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a8468a30c20'
down_revision = 'f20461bc808d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currencies', sa.Column('url', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'currencies', ['url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'currencies', type_='unique')
    op.drop_column('currencies', 'url')
    # ### end Alembic commands ###

"""First migration

Revision ID: f59e837ad635
Revises: f5524dd76310
Create Date: 2021-05-26 09:37:32.065056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f59e837ad635'
down_revision = 'f5524dd76310'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cleanings', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

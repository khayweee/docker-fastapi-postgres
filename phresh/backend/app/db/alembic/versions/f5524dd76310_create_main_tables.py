"""create_main_tables
Revision ID: f5524dd76310
Revises: 
Create Date: 2021-05-17 04:32:51.038471
"""

from alembic import op
import sqlalchemy as sa

def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

# revision identifiers, used by Alembic
revision = 'f5524dd76310'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    create_cleanings_table()
    
def downgrade() -> None:
    op.drop_table("cleanings")

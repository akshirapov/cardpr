"""Initial

Revision ID: e309c7c6693d
Revises:
Create Date: 2023-02-27 22:26:14.438746

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e309c7c6693d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "customer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("guid", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("surname", sa.String(length=50), nullable=False),
        sa.Column("middlname", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("phone", sa.String(length=12), nullable=False),
        sa.Column("birthday", sa.DateTime(), nullable=False),
        sa.Column("discount", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("bonus", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("balance", sa.Numeric(precision=15, scale=2), nullable=False),
        sa.Column("promo", sa.String(length=50), nullable=False),
        sa.Column("refer_customer_phone", sa.String(length=12), nullable=False),
        sa.Column("link", sa.Text(), nullable=False),
        sa.Column("form_url", sa.Text(), nullable=False),
        sa.Column("extra", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("guid"),
    )
    op.create_index(op.f("ix_customer_phone"), "customer", ["phone"], unique=False)

    op.create_table(
        "card",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("track", sa.String(length=50), nullable=False),
        sa.Column("install", sa.Boolean(), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("gpay_url", sa.Text(), nullable=False),
        sa.Column("customer_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("card")

    op.drop_index(op.f("ix_customer_phone"), table_name="customer")
    op.drop_table("customer")

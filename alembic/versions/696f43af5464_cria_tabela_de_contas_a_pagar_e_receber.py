"""Cria tabela de contas a pagar e receber

Revision ID: 696f43af5464
Revises: 
Create Date: 2023-02-05 16:07:34.222900

"""
from alembic import op
import sqlalchemy as sa

revision = '696f43af5464'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'contas_a_pagar_e_receber',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('descricao', sa.String(length=30), nullable=True),
        sa.Column('valor', sa.Numeric(), nullable=True),
        sa.Column('tipo', sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('contas_a_pagar_e_receber')

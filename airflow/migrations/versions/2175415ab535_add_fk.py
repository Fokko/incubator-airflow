#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Add FKs

Revision ID: 2175415ab535
Revises: 939bb1e647c8
Create Date: 2019-04-10 19:25:58.540765

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "2175415ab535"
down_revision = "939bb1e647c8"
branch_labels = None
depends_on = None


def upgrade():
    # create_foreign_key(
    #   constraint_name,
    #   referent_table,
    #   local_cols,
    #   remote_cols,
    #   referent_schema=None,
    #   onupdate=None,
    #   ondelete=None,
    #   deferrable=None,
    #   initially=None,
    #   match=None,
    #   **dialect_kw)¶
    with op.batch_alter_table("xcom") as batch_op:
        batch_op.create_foreign_key(
            "xcom_dag_id__dag_dag_id__fk",
            "dag",
            ["dag_id"],
            ["dag_id"],
            ondelete="CASCADE",
        )
    with op.batch_alter_table("task_instance") as batch_op:
        batch_op.create_foreign_key(
            "task_instance_job_id__job_id__fk",
            "job",
            ["job_id"],
            ["id"],
            ondelete="CASCADE",
        )

def downgrade():
    op.drop_constraint(None, "xcom_dag_id__dag_dag_id__fk", type_="foreignkey")
    op.drop_constraint(
        None, "xcom_task_id__task_instance_task_id__fk", type_="foreignkey"
    )

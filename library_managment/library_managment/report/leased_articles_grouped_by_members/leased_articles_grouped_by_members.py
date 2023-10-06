# Copyright (c) 2023, Malek and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"label": "Library Member", "fieldname": "library_member", "fieldtype": "Data"},
        {"label": "Article", "fieldname": "article_name", "fieldtype": "Data"},
    ]

    data = []

    articles = frappe.db.sql("""
        SELECT
            LT.library_member,
            A.article_name
        FROM
            `tabLibrary Transaction` LT
        INNER JOIN
            `tabArticle` A
        ON
            LT.article = A.name 
        WHERE
            A.status = 'Issued'
			AND LT.type = "Issue"
            AND LT.creation = (
                SELECT MAX(subLT.creation)
                FROM `tabLibrary Transaction` subLT
                WHERE subLT.article = A.name
                AND subLT.type = "Issue"
            )
        """, as_dict=True)

    for article in articles:
        data.append({
            "library_member": article["library_member"],
            "article_name": article["article_name"],
        })

    return columns, data


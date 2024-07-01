# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Lesson(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		academic_term: DF.Link
		academic_year: DF.Link
		course: DF.Link
		date: DF.Date
		faculty: DF.Link
		from_time: DF.Time
		group: DF.Data | None
		instructor: DF.Link
		lesson_type: DF.Literal["", "Ordinary Lesson", "Compensatory Lesson"]
		level: DF.Link
		program: DF.Link
		room: DF.Link
		schedule_template: DF.ReadOnly | None
		schedule_template_version: DF.Link
		to_time: DF.Time
	# end: auto-generated types
	pass
frappe.views.calendar["Appointment"] = {
    field_map: {
        start: "start_date",
        end: "end_date",
        id: "name",
        title: "title",
        allDay: "all_day",
        status: "status"
    },
    gantt: false,
    get_events_method: "frappe.desk.calendar.get_events",
    style_map: {
        "Scheduled": "orange",
        "Finished": "green",
        "Canceled": "red"
    }
};


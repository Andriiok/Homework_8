from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    current_date = date.today()
    next_week = current_date + timedelta(days=7)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekends = ['Saturday', 'Sunday']

    birthdays_per_week = {day: [] for day in weekdays + weekends}

    for user in users:
        name = user['name']
        birthday = user['birthday']

        bday_this_year = birthday.replace(year=current_date.year)

        if bday_this_year < current_date:
            bday_this_year = bday_this_year.replace(year=current_date.year + 1)

        if current_date <= bday_this_year < next_week:
            weekday_index = bday_this_year.weekday()
            weekday = weekdays[weekday_index]

            if weekday_index >= 5:  # Вихідний (субота або неділя)
                # Перенести вихідний день на понеділок
                weekday = weekdays[0]
                bday_this_year += timedelta(days=7 - weekday_index)

            if weekday == 'Monday' and (bday_this_year - current_date).days <= 2:
                # Додати до "Monday" дні народження цього тижня припалі на вихідні
                birthdays_per_week[weekdays[0]].append(name)
            elif weekday in weekdays:
                # Додати до відповідного дня тижня, якщо це не вихідний день
                birthdays_per_week[weekday].append(name)
            elif weekday == 'Saturday':
                # Додати до "Saturday" дні народження, якщо це вихідний
                birthdays_per_week[weekends[0]].append(name)
            elif weekday == 'Sunday':
                # Додати до "Sunday" дні народження, якщо це вихідний
                birthdays_per_week[weekends[1]].append(name)

    # Видаляємо ключі з порожніми списками
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

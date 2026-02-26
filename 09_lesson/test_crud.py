import uuid
from models import Student


def test_create_student(db):
    """Тест создания студента"""
    # Создаем уникальные данные
    email = f"test.{uuid.uuid4()}@mail.com"

    # Создаем студента
    student = Student(name="Тестовый Студент", age=20, email=email)
    db.add(student)
    db.commit()

    # Проверяем, что создался
    saved = db.query(Student).filter_by(email=email).first()
    assert saved is not None
    assert saved.name == "Тестовый Студент"
    assert saved.age == 20

    # Удаляем за собой
    db.delete(saved)
    db.commit()


def test_update_student(db):
    """Тест изменения студента"""
    # Сначала создаем студента
    email = f"update.{uuid.uuid4()}@mail.com"
    student = Student(name="Старое Имя", age=25, email=email)
    db.add(student)
    db.commit()

    # Меняем данные
    student.name = "Новое Имя"
    student.age = 26
    db.commit()

    # Проверяем изменения
    updated = db.query(Student).filter_by(email=email).first()
    assert updated.name == "Новое Имя"
    assert updated.age == 26

    # Удаляем за собой
    db.delete(updated)
    db.commit()


def test_delete_student(db):
    """Тест удаления студента"""
    # Создаем студента для удаления
    email = f"delete.{uuid.uuid4()}@mail.com"
    student = Student(name="Студент для удаления", age=22, email=email)
    db.add(student)
    db.commit()

    # Получаем ID созданного студента
    student_id = student.id

    # Удаляем студента
    db.delete(student)
    db.commit()

    # Проверяем, что удалился
    deleted = db.query(Student).filter_by(id=student_id).first()
    assert deleted is None

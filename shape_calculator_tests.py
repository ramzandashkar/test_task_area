import math
import logging
import unittest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ShapeCalculator:
    """
    Класс для вычисления площадей круга и треугольника.
    """

    @staticmethod
    def circle_area(radius: float) -> float:
        """
        Вычисляет площадь круга.

        :param radius: Радиус круга.
        :type radius: float
        :return: Площадь круга.
        :rtype: float
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        area = round(math.pi * radius ** 2, 2)
        logger.info(f"Вычислена площадь круга с радиусом {radius}: {area}")
        return area

    @staticmethod
    def triangle_area(side1: float, side2: float, side3: float) -> float:
        """
        Вычисляет площадь треугольника.

        :param side1: Длина первой стороны треугольника.
        :type side1: float
        :param side2: Длина второй стороны треугольника.
        :type side2: float
        :param side3: Длина третьей стороны треугольника.
        :type side3: float
        :return: Площадь треугольника.
        :rtype: float
        """
        if (side1 <= 0 or side2 <= 0 or side3 <= 0 or
                side1 + side2 <= side3 or side1 + side3 <= side2
                or side2 + side3 <= side1):
            # Добавил такой исключение, так как такие треугольники дают
            # значение "0", а значит такого треугольника не существует
            raise ValueError("Треугольник с такими сторонами не существует.")

        sides = [side1, side2, side3]
        sides.sort()

        if math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2):
            # Прямоугольный треугольник
            area = round(0.5 * sides[0] * sides[1], 2)
        else:
            # Произвольный треугольник
            s = (side1 + side2 + side3) / 2
            area = round(
                math.sqrt(s * (s - side1) * (s - side2) * (s - side3)), 2)

        logger.info(
            (f"Вычислена площадь треугольника со сторонами {side1}, {side2}, "
             f"{side3}: {area}")
        )
        return area


class TestShapeCalculator(unittest.TestCase):
    def test_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(6, 6, 6), 15.59)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(5, 5, 6), 12.0)
        with self.assertRaises(ValueError):
            ShapeCalculator.triangle_area(3, 4, 7)

    def test_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.circle_area(1), 3.14)
        self.assertAlmostEqual(ShapeCalculator.circle_area(2), 12.57)
        self.assertAlmostEqual(ShapeCalculator.circle_area(3), 28.27)
        self.assertAlmostEqual(ShapeCalculator.circle_area(4), 50.27)


if __name__ == "__main__":
    unittest.main()

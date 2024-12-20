class Polynomial:
    def __init__(self, coefficients):
        """
        Создает полином на основе списка коэффициентов.
        coefficients: список коэффициентов [с0, с1, ..., сn], где с0 - свободный член.
        """
        self._coefficients = coefficients

    @property
    def degree(self):
        """Возвращает степень полинома."""
        return len(self._coefficients) - 1

    def __repr__(self):
        """Строковое представление полинома."""

        terms = []
        degree = self.degree

        for power, coeff in enumerate(self._coefficients):

            if coeff != 0:
                if power == 0:
                    terms.append(f"{coeff}")
                elif power == 1:
                    if coeff == 1:
                        terms.append(f"x")
                    elif coeff == -1:
                        terms.append(f"-x")
                    else:
                        terms.append(f"{coeff}x")
                else:
                    if coeff == 1:
                        terms.append(f"x^{power}")
                    elif coeff == -1:
                        terms.append(f"-x^{power}")
                    else:
                        terms.append(f"{coeff}x^{power}")

        polynomial_str = " + ".join(terms).replace("+ -", "- ")
        return polynomial_str if terms else "0"

    def __call__(self, x):
        """Вычисляет значение полинома в точке x."""
        result = 0
        for power, coeff in enumerate(self._coefficients):
            result += coeff * (x ** power)
        return result
    def __add__(self, other):
        """Сложение двух полиномов."""
        max_len = max(len(self._coefficients), len(other._coefficients))
        new_coeffs = [0] * max_len

        for i in range(max_len):
            coeff1 = self._coefficients[i] if i < len(self._coefficients) else 0
            coeff2 = other._coefficients[i] if i < len(other._coefficients) else 0
            new_coeffs[i] = coeff1 + coeff2

        return Polynomial(new_coeffs)
    def __sub__(self, other):
        """Вычитание двух полиномов."""

        max_len = max(len(self._coefficients), len(other._coefficients))
        new_coeffs = [0] * max_len

        for i in range(max_len):
            coeff1 = self._coefficients[i] if i < len(self._coefficients) else 0
            coeff2 = other._coefficients[i] if i < len(other._coefficients) else 0
            new_coeffs[i] = coeff1 - coeff2

        return Polynomial(new_coeffs)
    def __mul__(self, other):
        """Умножение двух полиномов."""
        new_degree = self.degree + other.degree
        new_coeffs = [0] * (new_degree + 1)
        for i in range(len(self._coefficients)):
            for j in range(len(other._coefficients)):
                new_coeffs[i + j] += self._coefficients[i] * other._coefficients[j]
        return Polynomial(new_coeffs)

    def derivative(self):
        """Вычисляет производную полинома."""
        new_coeffs = []
        for i in range(1, len(self._coefficients)):
            new_coeffs.append(i * self._coefficients[i])
        return Polynomial(new_coeffs)

    def evaluate(self, x):
        """Вычисляет значение полинома в точке x."""


class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        """
        Квадратичный полином: должен быть степени 2.
        coefficients: список коэффициентов [c, b, a] для ax^2 + bx + c.
        """
        if len(coefficients) != 3:
            raise ValueError("Квадратичный полином должен иметь ровно 3 коэффициента.")
        super().__init__(coefficients)

    def discriminant(self):
        """Вычисляет дискриминант (b^2 - 4ac)."""
        a = self._coefficients[2]
        b = self._coefficients[1]
        c = self._coefficients[0]
        return b ** 2 - 4 * a * c
    def find_roots(self):
        """Находит корни квадратичного уравнения."""
        D = self.discriminant()  # Вычисляем дискриминант
        a = self._coefficients[2]  # Коэффициент a
        b = self._coefficients[1]  # Коэффициент b

        if D > 0:
            root1 = (-b + D**0.5) / (2 * a)
            root2 = (-b - D**0.5) / (2 * a)
            return (root1, root2)
        elif D == 0:
            root = -b / (2 * a)
            return (root,)


p1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
p2 = Polynomial([0, -1, 1]) # x^2 - x

print("P1:", p1)  # 3x^2 + 2x + 1
print("P2:", p2)   # x^2 - x
print("P1(2):", p1(2)) # 17
print("P1 + P2:", p1 + p2) # P1 + P2: 4x^2 + x + 1
print("P1 - P2:", p1 - p2) # P1 - P2: 2x^2 + 3x + 1
print("P1 * P2:", p1 * p2) # P1 * P2: 3x^4 - x^3 - x^2 - x
print("P1 derivative:", p1.derivative()) # P1 derivative: 6x + 2

test = QuadraticPolynomial([1, -3, 2])
print('Discriminant:', test.discriminant())
print('Roots:', test.find_roots())
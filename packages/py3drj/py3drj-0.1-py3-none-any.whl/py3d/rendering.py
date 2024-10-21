import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def render_model(model, color='cyan', alpha=0.7):
    """Рендеринг 3D-модели."""
    vertices = model.get_vertices()
    faces = model.get_faces()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        # Проверяем, что индексы в пределах массива вершин
        if all(0 <= idx < len(vertices) for idx in face):
            poly = Poly3DCollection([vertices[face]], alpha=alpha, facecolors=color)
            ax.add_collection3d(poly)
        else:
            print(f"Пропущена некорректная грань: {face}")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

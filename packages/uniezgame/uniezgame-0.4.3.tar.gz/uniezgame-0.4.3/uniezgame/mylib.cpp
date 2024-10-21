#include <pybind11/pybind11.h>
#include <SDL.h>
#include <iostream>
#include <memory>
#include <cmath>  // Dla std::sqrt
#include <array>

namespace py = pybind11;

int dodaj(int a, int b) {
    return a + b;
}

// Wrapper dla SDL_Renderer
class RendererWrapper {
public:
    RendererWrapper(SDL_Renderer* renderer) : renderer(renderer) {}
    ~RendererWrapper() {
        if (renderer) {
            SDL_DestroyRenderer(renderer);
        }
    }

    void clear() {
        SDL_RenderClear(renderer);
    }

    void present() {
        SDL_RenderPresent(renderer);
    }

    SDL_Renderer* get() const { return renderer; }

private:
    SDL_Renderer* renderer;
};

class Rect {
public:
    Rect(RendererWrapper& renderer, int x, int y, int width, int height, SDL_Color color)
        : renderer(renderer), x(x), y(y), width(width), height(height), color(color), angle(0.0f) {}

    void setAngle(float newAngle) {
        angle = newAngle;
    }

    void draw() {
        // Ustawienie koloru rysowania
        SDL_SetRenderDrawColor(renderer.get(), color.r, color.g, color.b, color.a);

        // Ustawienie prostok�ta
        SDL_Rect rect = { x, y, width, height }; // Ustawienie prostok�ta w centrum

        // Rysowanie prostok�ta bez obrotu
        SDL_RenderFillRect(renderer.get(), &rect);
    }

    void rotate(SDL_Rect rect) {
        // Ustawienie koloru rysowania
        SDL_SetRenderDrawColor(renderer.get(), color.r, color.g, color.b, color.a);

        // Rysowanie prostok�ta z obrotem
        SDL_RenderCopyEx(renderer.get(), nullptr, nullptr, &rect, angle, nullptr, SDL_FLIP_NONE);
    }

private:
    RendererWrapper& renderer;
    int x, y;            // Pozycja �rodka prostok�ta
    int width, height;   // Szeroko�� i wysoko�� prostok�ta
    SDL_Color color;     // Kolor prostok�ta
    float angle;         // K�t obrotu
};

// Funkcja do tworzenia okna i ustawiania koloru t�a
std::shared_ptr<RendererWrapper> create_window(int width, int height, int r, int g, int b, const std::string& title) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "Nie mo�na zainicjowa� SDL: " << SDL_GetError() << std::endl;
        return nullptr;
    }

    SDL_Window* window = SDL_CreateWindow(
        title.c_str(),
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        width,
        height,
        SDL_WINDOW_SHOWN
    );

    if (!window) {
        std::cerr << "Nie mo�na stworzy� okna: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return nullptr;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Nie mo�na stworzy� renderera: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return nullptr;
    }

    SDL_SetRenderDrawColor(renderer, r, g, b, 255);  // Ustaw kolor t�a
    SDL_RenderClear(renderer);  // Wyczy�� ekran
    SDL_RenderPresent(renderer);  // Wy�wietl zmiany

    // P�tla zdarze�, aby czeka� na zamkni�cie okna
    bool running = true;
    SDL_Event event;
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }
        SDL_Delay(16);  // Ma�e op�nienie dla zminimalizowania zu�ycia CPU (60 FPS)
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return std::make_shared<RendererWrapper>(renderer);
}

class Input {
public:
    Input() {
        keys.fill(false);
    }

    void Update() {
        std::fill(keys.begin(), keys.end(), false);

        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym < keys.size()) {
                    keys[event.key.keysym.sym] = true;
                }
            }
            else if (event.type == SDL_KEYUP) {
                if (event.key.keysym.sym < keys.size()) {
                    keys[event.key.keysym.sym] = false;
                }
            }

            if (event.type == SDL_MOUSEMOTION) {
                mouseX = event.motion.x;
                mouseY = event.motion.y;
            }
        }
    }

    bool isKeyPressed(int key) const {
        return key < keys.size() ? keys[key] : false;
    }

    int getMouseX() const { return mouseX; }
    int getMouseY() const { return mouseY; }

private:
    std::array<bool, 512> keys; // tablica klawiatury
    int mouseX = 0;
    int mouseY = 0;
};

PYBIND11_MODULE(uniezgame, m) {
    m.doc() = "Prosta biblioteka C++ dla Pythona";
    m.def("dodaj", &dodaj, "Funkcja dodaj�ca dwie liczby");

    py::class_<RendererWrapper, std::shared_ptr<RendererWrapper>>(m, "Renderer")
        .def("clear", &RendererWrapper::clear)
        .def("present", &RendererWrapper::present);

    py::class_<Rect>(m, "Rect")
        .def(py::init<RendererWrapper&, int, int, int, int, SDL_Color>(), "Tworzy nowy prostok�t")
        .def("Set_Angle", &Rect::setAngle, "Ustawia k�t obrotu")
        .def("Draw", &Rect::draw, "Rysuje prostok�t")
        .def("Rotate", &Rect::rotate, "Obraca prostok�t");

    // Dodajemy klas� Input do modu�u
    py::class_<Input>(m, "Input")
        .def(py::init<>())
        .def("update", &Input::Update, "Aktualizuje stan wej�cia")
        .def("is_key_pressed", &Input::isKeyPressed, "Sprawdza, czy klawisz jest wci�ni�ty",
            py::arg("key"))
        .def("get_mouse_x", &Input::getMouseX, "Zwraca pozycj� X myszy")
        .def("get_mouse_y", &Input::getMouseY, "Zwraca pozycj� Y myszy");

    m.def("create_window", &create_window, "Funkcja tworz�ca okno",
        py::arg("width"), py::arg("height"), py::arg("r"),
        py::arg("g"), py::arg("b"), py::arg("title"));
}

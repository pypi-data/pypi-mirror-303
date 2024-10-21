#include <pybind11/pybind11.h>
#include <SDL.h>
#include <iostream>
#include <memory>
#include <cmath>  // Dla std::sqrt
#include <array>
#include <tuple>

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

// Klasa do rysowania
class Draw {
public:
    Draw(RendererWrapper& renderer) : renderer(renderer) {}

    // Funkcja pomocnicza do konwersji krotki na SDL_Color
    SDL_Color create_color(int r, int g, int b, int a) {
        SDL_Color color;
        color.r = static_cast<Uint8>(r);
        color.g = static_cast<Uint8>(g);
        color.b = static_cast<Uint8>(b);
        color.a = static_cast<Uint8>(a);
        return color;
    }

    // Funkcja do rysowania prostok¹tów
    void Rect(int x, int y, int width, int height, const std::tuple<int, int, int, int>& colorTuple) {
        SDL_Color color = create_color(std::get<0>(colorTuple), std::get<1>(colorTuple), std::get<2>(colorTuple), std::get<3>(colorTuple));
        SDL_SetRenderDrawColor(renderer.get(), color.r, color.g, color.b, color.a);
        SDL_Rect rect = { x, y, width, height };
        SDL_RenderFillRect(renderer.get(), &rect);
    }

    // Funkcja do rysowania okrêgów
    void Circle(int centerX, int centerY, int radius, const py::tuple& color) {
        SDL_Color sdl_color;
        sdl_color.r = color[0].cast<Uint8>();
        sdl_color.g = color[1].cast<Uint8>();
        sdl_color.b = color[2].cast<Uint8>();
        sdl_color.a = color[3].cast<Uint8>();

        SDL_SetRenderDrawColor(renderer.get(), sdl_color.r, sdl_color.g, sdl_color.b, sdl_color.a);  // Ustaw kolor rysowania

        for (int w = 0; w < radius * 2; w++) {
            for (int h = 0; h < radius * 2; h++) {
                int dx = radius - w; // oblicz odleg³oœæ od œrodka
                int dy = radius - h;
                if ((dx * dx + dy * dy) <= (radius * radius)) {
                    SDL_RenderDrawPoint(renderer.get(), centerX + dx, centerY + dy); // Rysuj punkt
                }
            }
        }
    }

private:
    RendererWrapper& renderer; // Referencja do obiektu renderer
};

// Funkcja do tworzenia okna i ustawiania koloru t³a
std::shared_ptr<RendererWrapper> create_window(int width, int height, int r, int g, int b, const std::string& title) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "Nie mo¿na zainicjowaæ SDL: " << SDL_GetError() << std::endl;
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
        std::cerr << "Nie mo¿na stworzyæ okna: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return nullptr;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Nie mo¿na stworzyæ renderera: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return nullptr;
    }

    SDL_SetRenderDrawColor(renderer, r, g, b, 255);  // Ustaw kolor t³a
    SDL_RenderClear(renderer);  // Wyczyœæ ekran
    SDL_RenderPresent(renderer);  // Wyœwietl zmiany

    // Pêtla zdarzeñ, aby czekaæ na zamkniêcie okna
    bool running = true;
    SDL_Event event;
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }
        SDL_Delay(16);  // Ma³e opóŸnienie dla zminimalizowania zu¿ycia CPU (60 FPS)
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
            } else if (event.type == SDL_KEYUP) {
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
    m.def("dodaj", &dodaj, "Funkcja dodaj¹ca dwie liczby");

    py::class_<RendererWrapper, std::shared_ptr<RendererWrapper>>(m, "Renderer")
        .def("clear", &RendererWrapper::clear)
        .def("present", &RendererWrapper::present);

    py::class_<Draw>(m, "Draw")
        .def(py::init<RendererWrapper&>())
        .def("rect", &Draw::Rect, "Rysuje prostok¹t",
            py::arg("x"), py::arg("y"),
            py::arg("width"), py::arg("height"),
            py::arg("color"))
        .def("circle", &Draw::Circle, "Rysuje okr¹g",
            py::arg("centerX"), py::arg("centerY"),
            py::arg("radius"),
            py::arg("color"));

    // Dodajemy klasê Input do modu³u
    py::class_<Input>(m, "Input")
        .def(py::init<>())
        .def("update", &Input::Update, "Aktualizuje stan wejœcia")
        .def("is_key_pressed", &Input::isKeyPressed, "Sprawdza, czy klawisz jest wciœniêty",
            py::arg("key"))
        .def("get_mouse_x", &Input::getMouseX, "Zwraca pozycjê X myszy")
        .def("get_mouse_y", &Input::getMouseY, "Zwraca pozycjê Y myszy");

    m.def("create_window", &create_window, "Funkcja tworz¹ca okno",
        py::arg("width"), py::arg("height"), py::arg("r"),
        py::arg("g"), py::arg("b"), py::arg("title"));
}
 
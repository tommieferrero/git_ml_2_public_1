"""
Kommentar – Streamlit-app och begränsningar

I denna Streamlit-applikation använder jag samma ExtraTrees-modell och StandardScaler
som tränades i notebooken på MNIST-datasetet. Syftet är att kunna rita en egen siffra
(0–9) på en canvas och låta modellen göra en prediktion på denna nya indata.

Flödet i appen:
- Användaren ritar en siffra med vit penna på svart bakgrund i en 280×280 canvas.
- Bilden görs om till gråskala (L-läge i PIL).
- Jag hittar de pixlar som tillhör siffran genom ett tröskelvärde (mörk bakgrund
  tas bort, ljusare pixlar behålls).
- Runt dessa pixlar beräknas en bounding box, så att jag kan beskära bort onödig
  bakgrund.
- Den beskurna siffran skalas ned till en mindre bild (t.ex. 20–22 pixlar på
  största sidan) och placeras centrerad i en tom 28×28-bild. På så sätt försöker
  jag efterlikna hur MNIST-bilderna ser ut: vit siffra, svart bakgrund, centrerad.
- Den slutliga 28×28-bilden plattas ut till en vektor med 784 värden och skalanpassas
  med samma StandardScaler som modellen tränades med.
- Den skalade vektorn skickas in i ExtraTrees-modellen som sedan ger både en
  predikterad siffra och sannolikheter per klass. I appen visas även den nedskalade
  28×28-bilden så att man kan se hur modellen "ser" siffran.

Begränsningar:
I notebooken får modellen rena MNIST-bilder där siffrorna är centrerade, lagom
stora och skrivna med en viss stil. I Streamlit-appen ritar användaren fritt, vilket
gör att siffrorna kan bli tjockare, ha annan form eller hamna lite snett i rutan.
Trots beskärning och centrering i förbehandlingen är detta fortfarande en annan
datamängd än den modellen tränades på. Det är alltså ett exempel på domänskifte:
träningsdata och användardata skiljer sig åt.

ExtraTrees-modellen arbetar direkt på råa pixelvärden och har ingen inbyggd
invarians mot små förskjutningar eller stilskillnader, till skillnad från en
konvolutionell nätverksmodell (CNN). Detta märks särskilt för vissa siffror
som 6, 7 och 9, som i både confusion matrix från testdatan och i appen ofta
blandas ihop med andra klasser (t.ex. 6↔5/8, 7↔1, 9↔4/7). För andra siffror,
som 0, 1, 2, 3, 4, 5 och 8, fungerar modellen bättre även i appen när siffran
ritas tydligt.

Sammanfattningsvis:
- Modellen presterar mycket bra på MNIST-testdatan, vilket visas i notebooken.
- I Streamlit-appen sjunker prestandan på grund av att indata ser annorlunda
  ut än träningsdatan, trots att jag försöker efterlikna MNIST med beskärning
  och centrering.
- Appen fyller ändå sitt pedagogiska syfte: den visar hela kedjan från tränad
  modell, via sparade .joblib-filer, till en interaktiv gränssnitt där användaren
  kan rita siffror, se modellens prediktioner och samtidigt reflektera över
  generalisering, domänskifte och felklassificeringar.
"""

# streamlit run inlämning_streamlit_del_tommie_ferrero_1.py

import os
import numpy as np
import joblib
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# =========================
# Steg 1 – Ladda modell och scaler
# =========================

@st.cache_resource
def load_model_and_scaler():
    """
    Laddar den tränade ExtraTrees-modellen och StandardScaler
    från samma filer som sparades i notebooken.
    Söker relativt denna .py-fil så att det fungerar oavsett var appen startas ifrån.
    """
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "mnist_best_model.joblib")
    scaler_path = os.path.join(base_dir, "mnist_scaler.joblib")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_model_and_scaler()

# =========================
# Steg 2 – Layout och flikar
# =========================

st.title("MNIST – klassificering av handskrivna siffror")
st.write(
    "Denna Streamlit-app använder den tränade ExtraTrees-modellen "
    "för att klassificera handritade siffror (0–9) från MNIST."
)

tabs = st.tabs(["Rita siffra", "Webbkamera (framtida utveckling)"])

# =========================
# Hjälpfunktion – förbehandling med beskärning & centrering
# =========================

def preprocess_canvas_image(canvas_img, scaler):
    """
    Tar en 280x280-bild från canvas, hittar själva siffran,
    beskär runt den, centrerar i en 28x28-bild och skalar
    sedan med samma StandardScaler som i notebooken.
    """
    # 1. Gör om till gråskala (vit siffra på svart bakgrund)
    img = canvas_img.convert("L")  # 'L' = grayscale

    # 2. Till numpy-array (0–255)
    arr = np.array(img).astype("float32")

    # 3. Hitta pixlar där siffran finns (ljusare än bakgrunden)
    #    Tröskelvärdet 10 är ganska lågt, kan justeras vid behov.
    mask = arr > 10

    if not mask.any():
        # Om inget ritats: använd en helt svart 28x28 (modellen gissar ändå något)
        arr28 = np.zeros((28, 28), dtype="float32")
    else:
        # 4. Bounding box runt siffran
        ys, xs = np.where(mask)
        y_min, y_max = ys.min(), ys.max()
        x_min, x_max = xs.min(), xs.max()

        # 5. Beskär originalbilden till boxen
        cropped = arr[y_min:y_max + 1, x_min:x_max + 1]

        # 6. Skala beskärningen till max 20x20 för att lämna marginal
        target_inner_size = 20
        h, w = cropped.shape
        scale = target_inner_size / max(h, w)
        new_h = max(1, int(h * scale))
        new_w = max(1, int(w * scale))

        cropped_img = Image.fromarray(cropped).resize((new_w, new_h), Image.LANCZOS)
        cropped_resized = np.array(cropped_img).astype("float32")

        # 7. Lägg in den skalade siffran centrerad i en 28x28-bild
        arr28 = np.zeros((28, 28), dtype="float32")
        top = (28 - new_h) // 2
        left = (28 - new_w) // 2
        arr28[top:top + new_h, left:left + new_w] = cropped_resized

    # 8. Platta ut till (1, 784) och skala med StandardScaler
    img_flat = arr28.reshape(1, -1)
    img_scaled = scaler.transform(img_flat)

    return img_scaled, arr28

# =========================
# Flik 1 – Canvas för att rita siffror
# =========================

with tabs[0]:
    st.subheader("Rita en siffra")

    st.write(
        "Rita en siffra (0–9) i rutan nedan med vit penna på svart bakgrund, "
        "ungefär som i MNIST-datasetet."
    )

    canvas_size = 280  # 280x280 pixlar, skalas ned till 28x28
    stroke_width = 15
    stroke_color = "white"
    bg_color = "black"

    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_size,
        width=canvas_size,
        drawing_mode="freedraw",
        key="mnist_canvas",
    )

    st.caption(
        "Tips: Rita siffran ganska tjockt och centrera den i rutan för bäst resultat."
    )

    if st.button("Gör prediktion", key="predict_canvas"):
        if canvas_result.image_data is None:
            st.warning("Rita först en siffra i rutan.")
        else:
            # Canvas-data är RGBA-array (H, W, 4). Gör om till PIL-bild.
            canvas_data = canvas_result.image_data.astype("uint8")
            pil_img = Image.fromarray(canvas_data).convert("RGB")

            # Förbehandling (inkl. beskärning + centrering)
            x_scaled, img_28x28 = preprocess_canvas_image(pil_img, scaler)

            # Prediktion
            pred_class = model.predict(x_scaled)[0]
            proba = model.predict_proba(x_scaled)[0]

            st.subheader(f"Modellens prediktion: {pred_class}")

            st.write("Sannolikhet per siffra:")
            for digit, p in enumerate(proba):
                st.write(f"{digit}: {p:.3f}")

            st.subheader("Nedskalad 28×28-bild (som modellen ser den)")
            st.image(img_28x28, width=140, clamp=True)

# =========================
# Flik 2 – Webbkamera (placeholder)
# =========================

with tabs[1]:
    st.subheader("Webbkamera – planerad funktionalitet")
    st.write(
        "Här är det tänkt att man i framtiden ska kunna ta en bild med webbkamera, "
        "förbehandla den till 28×28 gråskala och använda samma modell för prediktion.\n\n"
        "I denna inlämning fokuserar jag på canvas-lösningen, men strukturen är "
        "förberedd för vidare utveckling."
    )

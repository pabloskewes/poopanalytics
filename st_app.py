import streamlit as st
data = None # DataFrame

user_names = data["users"].unique()


# Dropdown menu
option = st.selectbox(
    'Check user stats:',
    ('Option 1', 'Option 2', 'Option 3'))

# Display the chosen option
st.write('You selected:', option)


array(['Paula', 'pabloskewes', 'Albani', 'Cami Labarca', 'Asu',
       'Tomás Beauchef', 'Diego DCC', 'Julia', 'Bruno Rodriguez',
       '+56 9 9539 9283', 'Champi', 'Coti', '+33 6 95 21 23 51',
       'Seba Brzovic', 'Cebolla', 'Cholo', 'Vale Morado',
       '+56 9 6628 4408'], dtype=object)
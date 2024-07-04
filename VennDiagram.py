import streamlit as st
from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

def main():
    st.title("Venn Diagram Generator")
    
    st.sidebar.header("Input Parameters")
    num_sets = st.sidebar.selectbox("Number of Sets", [2, 3], index=0)
    
    bg_color = st.sidebar.color_picker("Background Color", "#ffffff")
    set1_color = st.sidebar.color_picker("Set A Color", "#ff9999")
    set2_color = st.sidebar.color_picker("Set B Color", "#9999ff")
    set3_color = st.sidebar.color_picker("Set C Color", "#99ff99") if num_sets == 3 else None

    if num_sets == 2:
        set_A_name = st.sidebar.text_input("Name of Set A", value="Set A")
        set_B_name = st.sidebar.text_input("Name of Set B", value="Set B")
        A = st.sidebar.number_input(f"Number of elements in {set_A_name}", min_value=0, value=0)
        B = st.sidebar.number_input(f"Number of elements in {set_B_name}", min_value=0, value=0)
        AB = st.sidebar.number_input(f"Number of elements in overlap of {set_A_name} and {set_B_name}", min_value=0, value=0)
        
        if st.sidebar.button("Generate Venn Diagram"):
            total = A + B + AB
            st.write(f"Total elements: {total}")
            st.write(f"{set_A_name}: {A} ({(A/total)*100:.2f}%)")
            st.write(f"{set_B_name}: {B} ({(B/total)*100:.2f}%)")
            st.write(f"Overlap of {set_A_name} and {set_B_name}: {AB} ({(AB/total)*100:.2f}%)")
            generate_venn2(A, B, AB, set_A_name, set_B_name, bg_color, set1_color, set2_color)
            
    elif num_sets == 3:
        set_A_name = st.sidebar.text_input("Name of Set A", value="Set A")
        set_B_name = st.sidebar.text_input("Name of Set B", value="Set B")
        set_C_name = st.sidebar.text_input("Name of Set C", value="Set C")
        A = st.sidebar.number_input(f"Number of elements in {set_A_name}", min_value=0, value=0)
        B = st.sidebar.number_input(f"Number of elements in {set_B_name}", min_value=0, value=0)
        C = st.sidebar.number_input(f"Number of elements in {set_C_name}", min_value=0, value=0)
        AB = st.sidebar.number_input(f"Number of elements in overlap of {set_A_name} and {set_B_name}", min_value=0, value=0)
        BC = st.sidebar.number_input(f"Number of elements in overlap of {set_B_name} and {set_C_name}", min_value=0, value=0)
        AC = st.sidebar.number_input(f"Number of elements in overlap of {set_A_name} and {set_C_name}", min_value=0, value=0)
        ABC = st.sidebar.number_input(f"Number of elements in overlap of {set_A_name}, {set_B_name}, and {set_C_name}", min_value=0, value=0)
        
        if st.sidebar.button("Generate Venn Diagram"):
            total = A + B + C + AB + BC + AC + ABC
            st.write(f"Total elements: {total}")
            st.write(f"{set_A_name}: {A} ({(A/total)*100:.2f}%)")
            st.write(f"{set_B_name}: {B} ({(B/total)*100:.2f}%)")
            st.write(f"{set_C_name}: {C} ({(C/total)*100:.2f}%)")
            st.write(f"Overlap of {set_A_name} and {set_B_name}: {AB} ({(AB/total)*100:.2f}%)")
            st.write(f"Overlap of {set_B_name} and {set_C_name}: {BC} ({(BC/total)*100:.2f}%)")
            st.write(f"Overlap of {set_A_name} and {set_C_name}: {AC} ({(AC/total)*100:.2f}%)")
            st.write(f"Overlap of {set_A_name}, {set_B_name}, and {set_C_name}: {ABC} ({(ABC/total)*100:.2f}%)")
            generate_venn3(A, B, C, AB, BC, AC, ABC, set_A_name, set_B_name, set_C_name, bg_color, set1_color, set2_color, set3_color)

def generate_venn2(A, B, AB, set_A_name, set_B_name, bg_color, set1_color, set2_color):
    plt.figure(figsize=(8, 6))
    plt.gca().set_facecolor(bg_color)
    venn = venn2(subsets=(A, B, AB), set_labels=(set_A_name, set_B_name))
    venn.get_patch_by_id('10').set_color(set1_color)
    venn.get_patch_by_id('01').set_color(set2_color)
    venn.get_patch_by_id('11').set_color("grey")  # Overlap color can be customized as needed
    st.pyplot(plt.gcf())
    plt.clf()

def generate_venn3(A, B, C, AB, BC, AC, ABC, set_A_name, set_B_name, set_C_name, bg_color, set1_color, set2_color, set3_color):
    plt.figure(figsize=(8, 6))
    plt.gca().set_facecolor(bg_color)
    venn = venn3(subsets=(A, B, C, AB, BC, AC, ABC), set_labels=(set_A_name, set_B_name, set_C_name))
    venn.get_patch_by_id('100').set_color(set1_color)
    venn.get_patch_by_id('010').set_color(set2_color)
    venn.get_patch_by_id('001').set_color(set3_color)
    venn.get_patch_by_id('110').set_color("grey")
    venn.get_patch_by_id('101').set_color("grey")
    venn.get_patch_by_id('011').set_color("grey")
    venn.get_patch_by_id('111').set_color("grey")  # Overlap colors can be customized as needed
    st.pyplot(plt.gcf())
    plt.clf()

if __name__ == "__main__":
    main()

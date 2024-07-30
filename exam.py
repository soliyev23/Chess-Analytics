import streamlit as st
import pandas as pd 
import string
import random
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df = pd.read_csv("chess_dataset.csv")

# Fixing sidebar:
st.set_page_config(layout="wide", page_title="GamersData", page_icon="*")
with st.sidebar:
    st.sidebar.image("https://flomaster.top/uploads/posts/2022-12/1672487847_flomaster-club-p-shakhmati-trafaret-instagram-15.png",width=250)
    selected = option_menu(menu_title=None,options=["About DataFrame", "Missing value", "Graphic analysis" ],default_index=0,)

if st.sidebar.button('FINISH'):
    st.balloons()





# Home
if selected == "About DataFrame":

    st.title("Welcome To My First Dashboar")
    st.write("### Here you can find information about online consignment of Chess")
    st.image("https://www.sports.ru/dynamic_images/post/312/498/0/share/20ab5b_no_logo_no_text.jpg")

    st.title("Lets getting acquainted with Data Frame")
    st.dataframe(df)

    st.write("## Any small statistics")



    column_1, column_2 = st.columns(2)

    with column_1:
        st.title("Rated or No?")
        fig = px.pie(df["rated"].value_counts(), values=df["rated"].value_counts(), names=df["rated"].value_counts().index,)
        st.plotly_chart(fig)
    with column_2:
        st.title("Who win?")
        fig = px.pie(df["winner"].value_counts(), values=df["winner"].value_counts(), names=df["winner"].value_counts().index)
        st.plotly_chart(fig)

    st.title("The End of game.")
    st.bar_chart(df.value_counts("victory_status",normalize=True)*100)


# Missin values
elif selected == "Missing value":
    st.title("Here we going to clean the dataframe")
    df = df.drop(columns="Unnamed: 0")
    st.dataframe(df)

    st.write("## Count of Nan")

    st.bar_chart(df.isna().sum())

    st.subheader('')
    with st.expander("## ID column:"):

    # Id nan qiymatlar orniga yangi id 
        st.write(f"Count of NaN: {df['id'].isna().sum()}")
        st.write(df[df["id"].isna()].head(2))
        st.write("Here i am going to generate a new indexes for nan values in id column")

        def generate_random_string(length=8):
            characters = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(characters) for _ in range(length))
            return random_string

        df["id"] = df["id"].apply(lambda x: generate_random_string(8) if pd.isna(x) else x)


    # Generate randome ni dashboard ga chiqarish
        def read_code(file_path, start_line, end_line):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return ''.join(lines[start_line:end_line])
        file_path = 'exam.py'
        start_line = 87
        end_line = 94

        code_snippet = read_code(file_path, start_line, end_line)

        st.code(code_snippet, language='python')

        st.write(f"Count of Nan: {df['id'].isna().sum()}")



    # Dublicate larni ochirish 

        st.write(f"Dublicated:  {df.duplicated().sum()}")
        st.write(df[df["id"] == "kWKvrqYL"])

        df = df.drop_duplicates(subset="id")

        st.code(read_code(file_path, 117,119),language="python")

        st.write(f"Dublicated:  {df.duplicated().sum()}")

#---NUMERIC COLUMN------------------------------------------------------------------------------------------

    # multiselect_choice = st.sidebar.multiselect('Multiselect', ['Mean', 'Median', 'Mode'])

    temp2 = df.select_dtypes("number").fillna(df.select_dtypes("number").median())


    st.title("Numeric columns")

    tab1, tab2, tab3 = st.tabs(["Mean","Median","Mode"])

    lst = df.select_dtypes("number").columns
    temp = df.select_dtypes("number") 



    with tab1:
        df_1 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mean()))
        df_1 = df_1.transform(lambda x: x.fillna(x.mean()))
        st.write(df_1.describe()-temp.describe())
    with tab2:
        df_2 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.median()))
        df_2 = df_2.transform(lambda x: x.fillna(x.mean()))
        st.write(df_2.describe()-temp.describe())
    with tab3:
        df_3 = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mode()))
        df_3 = df_3.transform(lambda x: x.fillna(x.mean()))
        st.write(df_3.describe()-temp.describe())

    st.code(read_code(file_path, 139,152),language="python")


    col1,col2 = st.columns(2)
    with col1:
        radio_choice = st. radio('Chose one of', ['Mean', 'Median', 'Mode'])
        if radio_choice == "Mean":
            pass
        if radio_choice == "Median":
            pass
        if radio_choice == "Mode":
            pass

        if st.button("Submit"):
            if radio_choice == "Mean":
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mean()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))

                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MEAN</p>',unsafe_allow_html=True)

            elif radio_choice == "Median":
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.median()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))
                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MEDIAN</p>',unsafe_allow_html=True)

            else:
                df[lst] = df.groupby(by=["victory_status"])[lst].transform(lambda x: x.fillna(x.mode()))
                df[lst] = df[lst].transform(lambda x: x.fillna(x.mean()))
                st.write('<p style="color:green; font-size:35px"> The Nan values is changed to MODE</p>',unsafe_allow_html=True)
    with col2:
        st.subheader('')
        with st.expander("Numeric isna:"):
            st.write(df[lst].isna().sum())


#---OBJECT COLUMN------------------------------------------------------------------------------------------
    st.title("Object columns")
    obj_column = ["victory_status","winner","increment_code","white_id","black_id","moves","opening_eco","opening_name"]
    st.dataframe(df[obj_column])



    df[obj_column] = df.groupby(by=["victory_status"])[obj_column].transform(lambda x: x.fillna(x.mode()[0]))
    df[obj_column] = df[obj_column].transform(lambda x: x.fillna(x.mode()[0]))

    st.code(read_code(file_path, 194,197),language="python")
    st.subheader('')
    with st.expander("Amount of Obj Nan"):
        st.write(df[obj_column].isna().sum())

    st.title("Boolean columns")
    
    df["rated"] = df.groupby(by=["victory_status"])["rated"].transform(lambda x: x.fillna(x.mode()[0]))
    df["rated"] = df["rated"].transform(lambda x: x.fillna(x.mode()[0]))

    st.code(read_code(file_path, 204,207),language="python")
    
    with st.expander("Amount of Nan"):
        st.write(df.isna().sum())



# TAHLIL FRAFIKALAR
elif selected == "Graphic analysis":
    df = df.drop(columns="Unnamed: 0")

    st.title('Chess Games Analysis')

    # Distribution of game results over time
    df['created_at'] = pd.to_datetime(df['created_at'], unit='ms')
    games_per_month = df.groupby(df['created_at'].dt.to_period('M')).size()

    fig,ax = plt.subplots(figsize=(10, 6))
    games_per_month.plot(kind='line',color="r",ax=ax,style="--",label="Count")
    ax.grid()
    ax.legend()
    ax.set_title("Distribution of Game Results Over Time",color="green")
    ax.set_xlabel('Time',color="green")
    ax.set_ylabel('Number of Games',color="green")
    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("")



    winner_counts = df['winner'].value_counts()
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=winner_counts.index, y=winner_counts.values, palette='viridis',ax=ax)
    ax.set_xlabel('Winner',color="r")
    ax.set_title('Number of Games Won by White vs. Black',color="r")
    ax.set_ylabel('Number of Games',color="r")
    st.pyplot(plt)


    # Distribution of game durations
    st.write("")
    st.write("## Here you can change color and bins of plot")
    col1,col2 = st.columns(2)
    with col1:
        bin = st.select_slider("select bin number",options=list(range(1, 30)),value=29 )
    
    with col2:
        color_picker_value = st.color_picker('Color picker',value="#0000FF")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['turns'], bins=bin, kde=True,ax=ax,color=color_picker_value)
    ax.set_title('Distribution of Game Durations (Turns)',color=color_picker_value)
    ax.set_xlabel('Number of Turns',color=color_picker_value)
    ax.set_ylabel('Number of games',color=color_picker_value)
    st.pyplot(plt)
    


    # Distribution of game durations for different victory statuses
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='turns', hue='victory_status', multiple='stack', bins=30)
    ax.set_title("Distribution of Game Durations for Different Victory Statuses",color="red")
    ax.set_xlabel('Number of Turns',color="red")
    ax.set_ylabel('Frequency',color="red")
    st.pyplot(plt)



    opening_counts = df['opening_name'].value_counts().head(10)
    fig,ax = plt.subplots(figsize=(12, 6))
    sns.barplot(y=opening_counts.index, x=opening_counts.values, palette='magma',ax=ax)
    ax.set_title("Most Common Openings")
    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Opening Name')
    st.pyplot(plt)


    white = df[df["winner"] == "white"]
    black = df[df["winner"] == "black"]
    
    fig,ax = plt.subplots(1,2, figsize=(12,6))

    fig.suptitle("Distribution of Player Ratings")
    sns.histplot(data=white, x="white_rating",ax=ax[0],bins=30,color="g")
    ax[0].set_title("White Rating")
    sns.histplot(data=black, x="black_rating",ax=ax[1],bins=30,color="Blue")
    ax[1].set_title("Black Rating")
    st.pyplot(fig)

    bin = st.select_slider("You can change the bins of plot",options=list(range(1, 85)),value=50)

    fig,ax = plt.subplots( figsize=(10,6))
    
    sns.histplot(data=white, x="white_rating", ax=ax,color="r",label="white_rating",bins=bin)
    sns.histplot(data=black, x="black_rating", ax=ax,color="Blue",label="black_rating",bins=bin)
    ax.legend()
    ax.set_title("Ratio of Black Rating and White Rating")
    ax.set_xlabel("Rating")

    st.pyplot(fig)

    # Heatmap
    st.header('Here you can chose a column and see correlation with each other')
    
    options = st.multiselect('Select multiple options to display:',df.select_dtypes("number").columns,default=["white_rating","black_rating"])

    
    correlation_matrix = df[options].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)






    











        

        



        






        



            

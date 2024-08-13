def wallpaper(background_image):
    styled = f"""
    <style>
        .stApp {{
            background: linear-gradient(rgba(15, 15, 15, 0.8), rgba(15, 15, 15, 0.8)), url(data:image/jpg;base64,{background_image});
            background-size: cover;
            color: #00ffea;
            font-family: 'Courier New', Courier, monospace;
        }}
        .content {{
            background: rgba(15, 15, 15, 0.9);
            padding: 30px;
            border-radius: 15px;
            border: 2px solid #00ffea;
            box-shadow: 0px 0px 20px #ff00ff;
        }}
        .title {{
            font-size: 48px;
            font-weight: bold;
            color: #ff00ff;
            text-align: center;
            text-shadow: 0px 0px 10px #ff00ff;
        }}
        .subtitle {{
            font-size: 24px;
            text-align: center;
            margin-bottom: 30px;
            color: #00ffea;
            text-shadow: 0px 0px 10px #00ffea;
        }}
        .divider {{
            border-top: 2px solid #ff00ff;
            margin: 20px 0;
        }}
        .input-label {{
            font-size: 18px;
            margin-bottom: 5px;
            color: #ff00ff;
            text-shadow: 0px 0px 10px #ff00ff;
        }}
        .prediction {{
            font-size: 36px;
            color: #00ffea;
            font-weight: bold;
            text-align: center;
            text-shadow: 0px 0px 20px #00ffea;
            animation: neonGlow 2s ease-in-out infinite alternate;
        }}
        @keyframes neonGlow {{
            from {{
                text-shadow: 0 0 20px #00ffea, 0 0 30px #00ffea, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 60px #ff00ff, 0 0 70px #ff00ff;
            }}
            to {{
                text-shadow: 0 0 30px #00ffea, 0 0 40px #00ffea, 0 0 50px #ff00ff, 0 0 60px #ff00ff, 0 0 70px #ff00ff, 0 0 80px #ff00ff;
            }}
        }}
        .footer {{
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #00ffea;
            text-shadow: 0px 0px 10px #00ffea;
        }}
        .pulse {{
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
    </style>
    """
    return styled

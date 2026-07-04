const express = require("express");
const cors = require("cors");
const axios = require("axios");
require("dotenv").config();

const app = express();

app.use(cors());
app.use(express.json());

app.post("/translate", async (req, res) => {

    try {

        const { text } = req.body;

        const response = await axios.post(
            "https://libretranslate.com/translate",
            {
                q: text,
                source: "en",
                target: "hi",
                format: "text"
            },
            {
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );

        res.json({
            translatedText: response.data.translatedText
        });

    } catch (error) {

        console.log(error.message);

        res.status(500).json({
            error: "Translation failed"
        });
    }
});

app.listen(process.env.PORT || 5000, () => {
    console.log("Server running on port 5000");
});
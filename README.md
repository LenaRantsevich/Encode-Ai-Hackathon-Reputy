# 🎉 Encode-Ai-Hackathon: Reputy.io 🤖

For all the recent graduates embarking on a job hunt, we are excited to introduce **Reputy**, a cutting-edge tool designed to revolutionize the way job seekers present themselves to potential employers. With Reputy, anyone can effortlessly showcase their diverse talents and soft skills, giving them that extra edge in today's competitive job market! 💼✨ Reputy Talent Wallet holds your reputation as personal currency.

## 🔍 Features Overview

- **Effortless CV Creation**: Highlighting not just professional achievements but also hobbies, interests, and lifestyle.
- **Social Media Integration**: Connect with ease to leverage online presence for career advancement.
- **Skill Highlighting**: Automatically analyze and incorporate relevant skills and experiences into your profile.
- **Control and Privacy**: Review and approve information before it's shared, ensuring accuracy and relevance.
- **Optimization Insights**: Receive tailored suggestions for enhancing online presence to align with career goals.

## 🛠️ Installation Guide

Get started with Reputy's frontend:

1. **Prerequisites**: Ensure you have Node.js and npm installed.
2. **Clone the Repository**: `git clone https://github.com/reputy/reputy-frontend`
3. **Navigate to Directory**: `cd reputy-frontend`
4. **Install Dependencies**: `npm install`
5. **Run the Application**: `npm start`

## 🚀 Workflow for Soft Skill Analysis Using AI 🧠🔍

### 1. Pre-processing 📊

- Extract essential metadata from the JSON file, focusing on post IDs and captions.
- Format the data for efficient processing, stripping it down to its core components.

### 2. Retrieval Augmented Generation (RAG) 🤖

- The formatted dataset is fed into OpenAI's GPT-4 LLM via the Assistants API as a temporary file.
- GPT-4's Retrieval Augmented Generation enhances model accuracy and prevents hallucination.
- The LLM is pre-prompted to analyze each of the Instagram post captions to identify represented soft skills.
- These detected soft skills are then prioritized based on the most represented 3 out of the 6 skills.

### 3. Post-processing ✨

- The model outputs the three most represented skills found in the analysis along with their post IDs.
- These skills, alongside relevant metadata like post images, are mapped using the post IDs.
- Finally, the findings are compiled into a JSON file for front-end integration.

## 🖥️ Usage Guide

Navigate Reputy's frontend with ease:

- **User Interface**: Intuitive design for seamless interaction.
- **Feature Interaction**: Effortlessly explore and utilize all functionalities.

## 📁 Folder Structure

Discover the frontend codebase organization:

- **Components**: Reusable UI components.
- **Pages**: Individual page components.
- **Utils**: Utility functions and helpers.

## 💻 Technologies Used

- **Languages**: HTML, CSS, JavaScript
- **Framework**: React.js
- **Dependencies**: OpenAI's GPT-4, Assistants API

## 🤝 Contributing Guidelines

Join us in enhancing Reputy:

- Submit bug reports, feature requests, or pull requests.
- Follow coding conventions and standards outlined in the repository.

## 📝 License

Reputy frontend is distributed under the MIT License.

## 📧 Contact

For inquiries or collaboration opportunities, reach out to us:

- Email: lena@reputy.io
- GitHub: @LenaRantsevich

## 🔗 Additional Resources

Explore the concept on our website:
www.reputy.io


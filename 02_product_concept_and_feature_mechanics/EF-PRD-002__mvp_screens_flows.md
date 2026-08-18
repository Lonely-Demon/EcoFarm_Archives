# MVP User Flows & Key Screens Outline

This document outlines the essential user flows and corresponding screens required for the Smart Farming Ecosystem MVP, based on the approved `mvp_feature_list.md` and the GrowWise UI/UX style.

## Core MVP Features (Reference)

1.  **Accurate Weather Data:** Display current and forecasted weather.
2.  **Farm/Field Mapping (Basic):** Allow users to define farm boundaries and basic field sectors (manual input/drawing for MVP).
3.  **AI Planting Recommendations (Location-Based):** Suggest crops based on location (public soil data estimate), weather, market data.
4.  **Marketplace (Basic):** View listings (buy/sell), potentially post simple listings.
5.  **Community Forum (Basic):** View posts, potentially post simple questions/updates.
6.  **User Account Management:** Login, registration, basic profile.
7.  **Notifications (Basic):** Weather alerts, potentially market updates.
8.  **Multi-Language Support:** Framework for future language additions.

## Key User Flows & Screens

**1. Onboarding & Authentication:**
    *   **Flow:** New user registration -> Login -> Existing user login.
    *   **Screens:**
        *   Splash Screen / Welcome Screen
        *   Login Screen (Email/Password, potentially Google/Social Login)
        *   Registration Screen (Basic info: Name, Email, Password, Location/Region)
        *   Password Reset Flow Screens (Forgot Password, Enter Code, Set New Password)

**2. Main Dashboard / Home:**
    *   **Flow:** User lands here after login. Provides an overview.
    *   **Screens:**
        *   **Home Dashboard:**
            *   Weather Summary Widget (Current temp, condition, link to detail)
            *   Quick Farm/Field Overview (e.g., total area, link to map/fields)
            *   Recent Notifications Snippet
            *   Potential shortcuts to key areas (Marketplace, Community, Recommendations)

**3. Weather Details:**
    *   **Flow:** Access from Dashboard widget or main navigation.
    *   **Screens:**
        *   **Weather Detail Screen:**
            *   Current conditions (temp, humidity, wind, etc.)
            *   Hourly forecast (next 24h)
            *   Daily forecast (next 5-7 days)

**4. Farm & Field Management (MVP Basic):**
    *   **Flow:** Add/View farm -> Define boundaries -> View fields -> Add/Edit basic field info.
    *   **Screens:**
        *   **My Fields / Farm Overview Screen:** List of fields, total area, potentially a small map overview.
        *   **Add/Edit Farm Screen:** Name, Location (potentially auto-detected or manual).
        *   **Map View Screen (Farm Boundary):** Interactive map to draw/edit farm boundaries (using map API tools).
        *   **Field Detail Screen:** View basic field info (Name, Area, Assigned Crop - manual for MVP).
        *   **Add/Edit Field Screen:** Name, Area (manual input or drawn on map), Crop selection (manual).

**5. AI Planting Recommendations:**
    *   **Flow:** User navigates to recommendations section -> Views suggestions based on their location/farm.
    *   **Screens:**
        *   **Recommendations Screen:**
            *   List of recommended crops for the user's region/location.
            *   Brief justification (e.g., suitable soil type estimate, favorable weather forecast, market demand indication).
            *   Disclaimer about recommendations being based on regional data.

**6. Marketplace (MVP Basic):**
    *   **Flow:** Browse listings -> View listing details -> (Optional MVP: Post simple listing).
    *   **Screens:**
        *   **Marketplace Feed Screen:** List/grid of buy/sell listings (e.g., produce, equipment) with images, titles, prices.
        *   **Listing Detail Screen:** Full details of a listing, contact information (if applicable).
        *   **(Optional MVP) Add Listing Screen:** Simple form to post a buy/sell listing (Title, Description, Price, Category, Image upload).

**7. Community Forum (MVP Basic):**
    *   **Flow:** Browse posts -> View post details/comments -> (Optional MVP: Post simple question/update).
    *   **Screens:**
        *   **Community Feed Screen:** List of posts/questions from other users.
        *   **Post Detail Screen:** Full post content and any comments.
        *   **(Optional MVP) Add Post Screen:** Simple form to create a new post/question.

**8. User Profile & Settings:**
    *   **Flow:** Access profile -> View/Edit details -> Access settings.
    *   **Screens:**
        *   **Profile Screen:** View user name, location, potentially farm summary.
        *   **Edit Profile Screen:** Update name, password, location.
        *   **Settings Screen:** Notification preferences, Language selection, Logout, About, Help/Support links.

**9. Notifications:**
    *   **Flow:** User receives push notifications -> Views notification list.
    *   **Screens:**
        *   **Notification List Screen:** Chronological list of received notifications (weather alerts, market updates, etc.).

## Navigation Structure (Mobile - Bottom Tab Bar)

*   Likely candidates for bottom tabs:
    1.  **Home/Dashboard**
    2.  **Fields/Map**
    3.  **Marketplace**
    4.  **Community**
    5.  **Profile/Settings**
*   (Weather and Recommendations might be accessed via Home or Profile/dedicated sections depending on final design).

This outline provides the basis for creating the initial wireframes.

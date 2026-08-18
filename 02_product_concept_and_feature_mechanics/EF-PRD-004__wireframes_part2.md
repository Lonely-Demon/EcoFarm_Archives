# Low-Fidelity Wireframes (MVP - Part 2)

Continuing from `wireframes_part1.md`, based on `mvp_screens_flows.md` and GrowWise style inspiration.

## 3. Weather Details

**Screen: Weather Detail Screen**

*   **Layout:** Vertical stack, potentially with tabs or segments for Hourly/Daily.
*   **Elements:**
    *   [Header: Weather in [Location]]
    *   **[Current Conditions Section]**
        *   [Large Text: Current Temperature]
        *   [Icon: Current Condition]
        *   [Text: Feels Like Temp]
        *   [Text: Humidity]
        *   [Text: Wind Speed/Direction]
        *   [Text: Precipitation Chance]
    *   **[Hourly Forecast Section]**
        *   [Horizontal Scrollable List/Chart]
            *   [Item: Hour 1 (Time, Icon, Temp)]
            *   [Item: Hour 2 (Time, Icon, Temp)]
            *   [...]
    *   **[Daily Forecast Section]**
        *   [Vertical List]
            *   [List Item: Day 1 (Day Name, Icon, High/Low Temp)]
            *   [List Item: Day 2 (Day Name, Icon, High/Low Temp)]
            *   [...]
    *   [Bottom Navigation Bar (Visible)]

## 4. Farm & Field Management (MVP Basic)

**Screen: My Fields / Farm Overview Screen**

*   **Layout:** List of field cards, potentially with a summary card at the top.
*   **Elements:**
    *   [Header: My Fields]
    *   [Button: Add New Field (+ Icon)]
    *   **[Summary Card (Optional)]**
        *   [Text: Total Farm Area]
        *   [Text: Number of Fields]
    *   **[Field Card 1]**
        *   [Small Map Thumbnail of Field]
        *   [Text: Field Name (e.g., Wheat Field)]
        *   [Text: Crop (e.g., Wheat)]
        *   [Text: Area (e.g., 20 ha)]
        *   [Link/Arrow: View Details >]
    *   **[Field Card 2]**
        *   [...]
    *   [Bottom Navigation Bar (Visible, Fields Tab Active)]

**Screen: Map View Screen (Farm Boundary/Field Drawing)**

*   **Layout:** Full-screen map interface.
*   **Elements:**
    *   [Header: Define Farm Boundary / Draw Field Area]
    *   [Map View (Interactive - Google Maps/Other)]
    *   [Map Controls: Zoom In/Out, My Location]
    *   [Drawing Tools (Icons): Add Point, Undo, Clear]
    *   [Instruction Text: Tap points to draw boundary...]
    *   [Button: Save Boundary / Save Field Area (Primary)]
    *   [Button: Cancel]

**Screen: Field Detail Screen**

*   **Layout:** Card-based detail view.
*   **Elements:**
    *   [Header: [Field Name]]
    *   **[Map Card]**
        *   [Static Map View of Field Boundary]
    *   **[Details Card]**
        *   [Label: Crop]
        *   [Value: [Crop Name]]
        *   [Label: Area]
        *   [Value: [Area Size]]
        *   [Label: Notes (Optional)]
        *   [Value: [User Notes Text Area]]
    *   [Button: Edit Field]
    *   [Bottom Navigation Bar (Visible)]

**Screen: Add/Edit Field Screen**

*   **Layout:** Form within a screen.
*   **Elements:**
    *   [Header: Add New Field / Edit Field]
    *   [Text Input: Field Name]
    *   [Button: Draw Field Area on Map]
    *   [Text Input: Area (Manual Entry - Alternative/Fallback)]
    *   [Dropdown/Selector: Assign Crop]
    *   [Text Area: Notes (Optional)]
    *   [Button: Save Field (Primary)]
    *   [Button: Cancel]

## 5. AI Planting Recommendations

**Screen: Recommendations Screen**

*   **Layout:** List of recommendation cards.
*   **Elements:**
    *   [Header: Planting Recommendations for [Location]]
    *   [Text: Based on regional soil estimates, weather forecast, and market trends.]
    *   [Disclaimer Text: These are suggestions. Consider local conditions.]
    *   **[Recommendation Card 1]**
        *   [Text: Recommended Crop Name]
        *   [Icon: Crop Type]
        *   [Text: Reason Snippet (e.g., Good soil match, Favorable forecast)]
        *   [Link/Arrow: View Details > (Optional)]
    *   **[Recommendation Card 2]**
        *   [...]
    *   [Bottom Navigation Bar (Visible)]

## 6. Marketplace (MVP Basic)

**Screen: Marketplace Feed Screen**

*   **Layout:** Grid or list of listing cards.
*   **Elements:**
    *   [Header: Marketplace]
    *   [Search Bar (Optional)]
    *   [Filters/Categories (Optional)]
    *   [Button: Post New Listing (+ Icon)]
    *   **[Listing Card 1]**
        *   [Image Thumbnail]
        *   [Text: Listing Title]
        *   [Text: Price]
        *   [Text: Location/Seller Snippet]
    *   **[Listing Card 2]**
        *   [...]
    *   [Bottom Navigation Bar (Visible, Market Tab Active)]

**Screen: Listing Detail Screen**

*   **Layout:** Detail view, likely scrollable.
*   **Elements:**
    *   [Header: [Listing Title]]
    *   [Image Carousel/Large Image]
    *   [Text: Price]
    *   [Text: Description]
    *   [Text: Category]
    *   [Text: Seller Information / Location]
    *   [Button: Contact Seller (if applicable)]

**(Optional MVP) Screen: Add Listing Screen**

*   **Layout:** Form.
*   **Elements:**
    *   [Header: Create New Listing]
    *   [Dropdown: Category (Buy/Sell, Produce/Equipment)]
    *   [Text Input: Title]
    *   [Text Area: Description]
    *   [Text Input: Price]
    *   [Button: Upload Image(s)]
    *   [Text Input: Contact Info/Location]
    *   [Button: Post Listing (Primary)]

## 7. Community Forum (MVP Basic)

**Screen: Community Feed Screen**

*   **Layout:** List of post cards.
*   **Elements:**
    *   [Header: Community Forum]
    *   [Button: Ask Question / New Post (+ Icon)]
    *   **[Post Card 1]**
        *   [User Avatar/Name]
        *   [Timestamp]
        *   [Post Title/Snippet]
        *   [Metrics: Likes/Comments Count]
    *   **[Post Card 2]**
        *   [...]
    *   [Bottom Navigation Bar (Visible, Community Tab Active)]

**Screen: Post Detail Screen**

*   **Layout:** Detail view with comments below.
*   **Elements:**
    *   [Header: [Post Title]]
    *   **[Original Post Section]**
        *   [User Avatar/Name]
        *   [Timestamp]
        *   [Full Post Content]
        *   [Like Button]
    *   **[Comments Section]**
        *   [Comment Input Area]
        *   [List of Comments]
            *   [Comment 1 (User, Timestamp, Text)]
            *   [Comment 2 (...)]

**(Optional MVP) Screen: Add Post Screen**

*   **Layout:** Form.
*   **Elements:**
    *   [Header: Create New Post]
    *   [Text Input: Title (Optional)]
    *   [Text Area: Your question or update...]
    *   [Button: Add Image (Optional)]
    *   [Button: Post (Primary)]

## 8. User Profile & Settings

**Screen: Profile Screen**

*   **Layout:** Card-based sections.
*   **Elements:**
    *   [Header: Profile]
    *   **[User Info Card]**
        *   [User Avatar]
        *   [Text: User Name]
        *   [Text: Email]
        *   [Text: Location/Region]
        *   [Button: Edit Profile]
    *   **[Farm Summary Card (Optional)]**
        *   [Text: Total Farm Area]
        *   [Text: Number of Fields]
    *   **[Settings Links/Section]**
        *   [Link: Notifications]
        *   [Link: Language]
        *   [Link: Help & Support]
        *   [Link: About]
    *   [Button: Logout]
    *   [Bottom Navigation Bar (Visible, Profile Tab Active)]

**Screen: Settings Screen (Example: Notifications)**

*   **Layout:** List of toggle switches/options.
*   **Elements:**
    *   [Header: Notification Settings]
    *   [Toggle Switch + Label: Weather Alerts]
    *   [Toggle Switch + Label: Market Updates]
    *   [Toggle Switch + Label: Community Activity]
    *   [Button: Save Changes]

## 9. Notifications

**Screen: Notification List Screen**

*   **Layout:** Chronological list.
*   **Elements:**
    *   [Header: Notifications]
    *   [Button: Mark All as Read (Optional)]
    *   **[Notification Item 1]**
        *   [Icon: Notification Type (Weather/Market/Community)]
        *   [Text: Notification Title/Snippet]
        *   [Timestamp]
    *   **[Notification Item 2]**
        *   [...]

*(End of Wireframes Part 2)*

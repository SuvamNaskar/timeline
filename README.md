# TimeLine - Social Media Platform

A modern, responsive social media platform built with Django and TailwindCSS.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, Instagram-inspired interface with dark theme
- **Interactive Elements**: Like buttons, story navigation, mobile sidebar
- **Accessibility**: Focus states, keyboard navigation, high contrast support
- **Performance**: Optimized loading, smooth animations, efficient DOM handling

## Project Structure

```
home-server/
├── home/                   # Main Django app
│   ├── templates/         # HTML templates
│   │   ├── base.html     # Base template with navigation
│   │   └── index.html    # Home page with feed
│   ├── views.py          # View functions
│   └── ...
├── home_server/          # Django project settings
├── static/               # Static files (CSS, JS, images)
├── media/               # User-uploaded media files
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## Setup Instructions

1. **Install Python** (3.8 or higher)

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**: http://127.0.0.1:8000/

## Key Components

### Navigation
- **Desktop**: Fixed sidebar with main navigation
- **Mobile**: Hamburger menu opens slide-out sidebar
- **Bottom Navigation**: Mobile-friendly bottom navigation bar

### Responsive Features
- **Stories**: Horizontal scrollable story section
- **Feed**: Responsive post cards with like/comment functionality
- **Sidebar**: Collapsible on mobile, suggestions section on desktop

### Interactions
- **Like Animation**: Heart animation with color change
- **Story Scroll**: Mouse drag and touch support
- **Mobile Menu**: Smooth slide transitions
- **Loading States**: User feedback for actions

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Features

- Intersection Observer for scroll animations
- Efficient event delegation
- Optimized CSS with hardware acceleration
- Preloaded critical resources

## Accessibility Features

- Keyboard navigation support
- Focus indicators
- High contrast mode support
- Reduced motion support
- ARIA labels and semantic HTML

## Future Enhancements

- User authentication system
- Real-time messaging
- Image upload functionality
- Infinite scroll feed
- Push notifications
- Progressive Web App (PWA) features

## Development Notes

- Uses Django's template system for server-side rendering
- TailwindCSS for utility-first styling
- Vanilla JavaScript for interactions (no frameworks)
- Mobile-first responsive design approach
- Modern CSS features with fallbacks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test responsiveness across devices
5. Submit a pull request

## License

This project is open source and available under the MIT License.

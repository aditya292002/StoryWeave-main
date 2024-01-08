import React from 'react';
import bgVideo from '../assets/mp4/bg.mp4'; // Import the video file


const Home = () => {
    return (
      <div style={{ position: 'relative', overflow: 'hidden', height:'auto'}}>
        {/* Background Video */}
        <video
          className="bg-video"
          playsInline
          autoPlay
          muted
          loop
          style={{
            width: '100%',
            height: 'auto',
            position: 'absolute',
            top: 0,
            left: 0,
          }}
        >
          <source src={bgVideo} type="video/mp4" />
        </video>
  
        {/* Overlay for the masthead */}
        <div
          style={{
            position: 'absolute',
            top: 0,
            bottom: 0,
            right: 0,
            left: 0,
            height: '100%',
            width: '100%',
            backgroundColor: 'rgba(0, 0, 0, 0.15)', // Similar to fade-out($black, 0.15)
          }}
        ></div>
  
        {/* Masthead content element */}
        <div
          className="masthead-content"
          style={{
            position: 'relative',
            maxWidth: '40rem',
            paddingTop: '5rem',
            paddingBottom: '5rem',
            textAlign: 'center',
            color: 'white',
            zIndex: 3, // Make sure it's above the overlay
            margin: 'auto', // Center the content
          }}
        >
          {/* <h1 style={{ fontSize: '2rem' }}>Welcome to WitQuiz Whiz</h1>
          <p style={{ fontSize: '1.2rem' }}>
          Unleash the Power of Knowledge with [Your App Name], your go-to platform for dynamic and engaging quizzes! Whether you're a content creator, educator, or just someone passionate about learning, our app transforms text content into interactive quizzes effortlessly.
          </p> */}
      <div style={{ position: 'relative', zIndex: 1 }}>
        <h1 className="display-3" style={{ fontWeight: 'bold' }}>
          Transform Data into Interactive Experiences
        </h1>
        <br />
        <p className="lead" style={{ fontStyle: 'italic', fontWeight: 'bold' }}>
          Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions
          effortlessly.
        </p>
        <br />
        <a className="btn btn-primary btn-lg" href="/quiz" role="button">
          Try it
        </a>
      </div>
        </div>
      </div>
    );
  };

export default Home;

import React from 'react';
import appLogo from '../assets/img/app_logo.jpg';
import john from '../assets/img/John_Doe.jpg';
import jane from '../assets/img/Jane_smith.jpg';


const About = () => {
  return (
    <div style={{background:"#f8edeb", position: 'relative', overflow: 'hidden' }}>



      {/* Masthead content element */}
      <div
        className="masthead-content"
        style={{
          position: 'relative',
          maxWidth: '40rem',
          paddingTop: '5rem',
          paddingBottom: '5rem',
          textAlign: 'center',
          color: 'Black',
          zIndex: 3, // Make sure it's above the overlay
          margin: 'auto', // Center the content
        }}
      >
        <img
          src={appLogo}
          alt="Company Logo"
          style={{ maxWidth: '10%', height: 'auto', borderRadius: '50%', border: '2px solid white' }}
        />

        <p style={{ marginTop: '2rem', marginLeft:'2rem', fontSize: '1.2rem', lineHeight: '1.6' }}>
          Welcome to WitQuiz Whiz! We are a passionate team dedicated to [describe your mission or purpose]. Our journey
          began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight your core
          values and goals].
        </p>

        <p style={{ marginTop: '2rem', fontSize: '1.2rem', lineHeight: '1.6' }}>Our Team:</p>

        {/* Team Member 1 */}
        <div className="card mb-3" style={{ marginTop: '1rem', marginLeft: '7rem', maxWidth: '400px', backgroundColor: 'rgba(0, 0, 0, 0.7)', borderRadius: '15px' }}>
          <div className="row g-0 align-items-center">
            <div className="col-md-4">
              <img
                src={john}
                alt="Team Member 1"
                className="img-fluid"
                style={{ maxWidth: '100%', height: 'auto', borderRadius: '50%', border: '2px solid white' }}
              />
            </div>
            <div className="col-md-8">
              <div className="card-body text-white">
                <h5 className="card-title">John Doe</h5>
                <p className="card-text" style={{ fontSize: '1rem', lineHeight: '1.4', textAlign:'left'}}>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et
                  dolore magna aliqua.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Team Member 2 */}
        <div className="card mb-3" style={{ maxWidth: '400px',marginLeft: '7rem', backgroundColor: 'rgba(0, 0, 0, 0.7)', borderRadius: '15px' }}>
          <div className="row g-0 align-items-center">
            <div className="col-md-4">
              <img
                src={jane}
                alt="Team Member 2"
                className="img-fluid"
                style={{ maxWidth: '100%', height: 'auto', borderRadius: '50%', border: '2px solid white' }}
              />
            </div>
            <div className="col-md-8">
              <div className="card-body text-white">
                <h5 className="card-title">Jane Smith</h5>
                <p className="card-text" style={{ fontSize: '1rem', lineHeight: '1.4', textAlign:'left'}}>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et
                  dolore magna aliqua.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

import octofitLogo from '../public/octofitapp-small.svg';

function App() {
  return (
    <Router>
      <div className="App bg-light min-vh-100">
        {/* Bootstrap Navbar */}
        <nav className="navbar navbar-expand-lg navbar-dark">
          <div className="container-fluid">
            <a className="navbar-brand d-flex align-items-center" href="#">
              <img src={octofitLogo} alt="Octofit Logo" className="octofit-logo me-2" />
              Octofit Tracker
            </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <a className="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#activities">Activities</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#teams">Teams</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#leaderboard">Leaderboard</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#workouts">Workouts</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#users">Users</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        <main className="container py-4">
          <div className="row justify-content-center">
            <div className="col-md-10">
              <div className="card shadow-sm">
                <div className="card-body">
                  <h1 className="display-4 text-center mb-4">Welcome to Octofit Tracker</h1>
                  {/* Main content and routed components will go here */}
                  <p className="lead text-center">Track your fitness, join teams, and compete on the leaderboard!</p>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;

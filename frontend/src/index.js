import React from "react";
import ReactDOM  from "react-dom/client";
import { Route, createBrowserRouter, createRoutesFromElements } from "react-router-dom";
import Layout from "./components/layout";
import Home from "./components/home";
import About from "./components/about";
import ProcessLogin from "./components/process_login";
import Choice from "./components/choice";
import { RouterProvider } from "react-router-dom";


const router = createBrowserRouter(
  createRoutesFromElements(
      <Route path='/' element={<Layout style={{margin:'0'}} />}>
          <Route path='' element={<Home />} />
          <Route path='about' element={<About />} />
          <Route path='login' element={<ProcessLogin />} />
          <Route path='Room' element={<Choice />} />
      </Route>
  )
)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <React.StrictMode>
        <RouterProvider router={router} />
  // </React.StrictMode>
);
    


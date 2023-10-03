import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const user = store.user;
	console.log(user);
	const navigate = useNavigate();

	function handleLogout() {
		actions.logout();
		if (user !== null) {
			navigate("/");
		} 
	}


	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">Home</span>
				</Link>
				<div className="ml-auto">
					{ user == null ? 
					<Link to="/login">
						<button className="btn btn-primary">Login</button>
					</Link>
					:
					<button type="button" className="btn btn-danger" onClick={handleLogout} >Logout</button>
					}
					
				</div>
			</div>
		</nav>
	);
};

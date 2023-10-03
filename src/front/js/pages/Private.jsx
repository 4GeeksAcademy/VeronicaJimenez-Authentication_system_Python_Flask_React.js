import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Private = props => {
	const { store, actions } = useContext(Context);
	const user = store.user;
	const navigate = useNavigate();

	if (user == null) {
		navigate("/login");
	} 

	return (
		<div className="text-center my-5">
			<h1>This is a private page</h1>
		</div>
	);
};
import React from "react";
import Checker from "../components/Checker";
import {render} from "@testing-library/react";

import 'mutationobserver-shim';

import {IFormProp} from "../types/interfaces"

function renderChecker(props: IFormProp) {
    return render(<Checker {...props} />);
}

describe("<TopSearched />", () => {

    test("should display initial screen", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : false,
            "isSubmitted":false,
            "isAnagram":false,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).not.toBeDisabled();
        expect(getByTestId("formInput2")).not.toBeDisabled();
        expect(queryByText("Submit")).toBeTruthy();
        expect(queryByText("YES")).toBeFalsy();
        expect(queryByText("NO")).toBeFalsy();
    });

    test("first submit before response", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : true,
            "isSubmitted":false,
            "isAnagram":false,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).toBeDisabled();
        expect(getByTestId("formInput2")).toBeDisabled();
        expect(queryByText("Loading…")).toBeTruthy();
        expect(queryByText("YES")).toBeFalsy();
        expect(queryByText("NO")).toBeFalsy();
    });

    test("after first response true", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : false,
            "isSubmitted":true,
            "isAnagram":true,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).not.toBeDisabled();
        expect(getByTestId("formInput2")).not.toBeDisabled();
        expect(queryByText("Submit")).toBeTruthy();
        expect(queryByText("YES")).toBeTruthy();
        expect(queryByText("NO")).toBeFalsy();
    });

    test("after first response false", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : false,
            "isSubmitted":true,
            "isAnagram":false,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).not.toBeDisabled();
        expect(getByTestId("formInput2")).not.toBeDisabled();
        expect(queryByText("Submit")).toBeTruthy();
        expect(queryByText("YES")).toBeFalsy();
        expect(queryByText("NO")).toBeTruthy();
    });

    test("second+ submit before response (first submit true)", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : true,
            "isSubmitted":true,
            "isAnagram":true,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).toBeDisabled();
        expect(getByTestId("formInput2")).toBeDisabled();
        expect(queryByText("Loading…")).toBeTruthy();
        expect(queryByText("YES")).toBeFalsy();
        expect(queryByText("NO")).toBeFalsy();
    });

    test("second+ submit before response (first submit false)", async () => {
        const mockOnSubmit = jest.fn();

        const prop = {
            "isLoading" : true,
            "isSubmitted":true,
            "isAnagram":false,
            "onSubmit":mockOnSubmit
        }

        const {queryByText, getByTestId} = renderChecker(prop);
        
        expect(queryByText("Word 1")).toBeTruthy();
        expect(queryByText("Word 2")).toBeTruthy();
        expect(getByTestId("formInput1")).toBeDisabled();
        expect(getByTestId("formInput2")).toBeDisabled();
        expect(queryByText("Loading…")).toBeTruthy();
        expect(queryByText("YES")).toBeFalsy();
        expect(queryByText("NO")).toBeFalsy();
    });
});
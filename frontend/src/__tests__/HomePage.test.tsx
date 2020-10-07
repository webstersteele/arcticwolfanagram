import React from "react";
import HomePage from "../components/HomePage";
import {render} from "@testing-library/react";
import axios from 'axios';

jest.mock('axios');

describe("<HomePage />", () => {

    test("should display initial screen", async () => {
        const mockedResponse = {
            "isAnagram": true
        }
        axios.post = jest.fn().mockResolvedValue(mockedResponse);

        const {} = render(<HomePage />);
        
        // fireEvent.click(getByText('Submit'));
        
        // expect(await mockOnSubmit).toBeCalled();
    });
});
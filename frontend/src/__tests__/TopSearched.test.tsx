import React from "react";
import TopSearched from "../components/TopSearched";
import { render, within} from "@testing-library/react";

import 'mutationobserver-shim';

import {ITableProp} from "../types/interfaces"

function renderTopSearch(props: (ITableProp | undefined)) {
    const defaultProps: ITableProp = {
        anagramList: []
    }

    return render(<TopSearched {...defaultProps} {...props} />);

}

describe("<TopSearched />", () => {
  test("should display a blank Table, with error line", async () => {
    const { queryByText, getAllByRole} = renderTopSearch(undefined);
    
    const rows = getAllByRole("row");

    expect(rows.length=1)

    expect(queryByText("No anagrams have been submitted.")).toBeTruthy();
  });

  test("should display 3 rows, with correct information", async () => {
    
    const tupple1: [string, string] = ["this", "that"]
    const tupple2: [string, string] = ["other", "thing"]
    const tupple3: [string, string] = ["shouldBe", "last"]
    
    const defaultProp = {
        "anagramList": [
            {
                "words": tupple1,
                "frequency": 10
            },
            {
                "words": tupple2,
                "frequency": 4
            },
            {
                "words": tupple3,
                "frequency": 3
            }
        ]
    }

    const {getAllByRole} = renderTopSearch(defaultProp);
    
    const rows = getAllByRole("row");

    expect(rows.length=3)
    
    within(rows[0]).findByText("1")
    within(rows[0]).findByText("this")
    within(rows[0]).findByText("that")
    within(rows[0]).findByText("10")

    within(rows[1]).findByText("2")
    within(rows[1]).findByText("other")
    within(rows[1]).findByText("thing")
    within(rows[1]).findByText("4")

    within(rows[2]).findByText("3")
    within(rows[2]).findByText("shouldBe")
    within(rows[2]).findByText("last")
    within(rows[2]).findByText("3")

  });
});
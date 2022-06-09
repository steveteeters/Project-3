# Project-3
---
![logo (2)](https://user-images.githubusercontent.com/95944553/169931289-f562db29-e5bd-4839-88af-56aebb63d78e.svg)
---
Create a blockchain for the mining and distribution of donations from the donor to the end recipient. We will create a main account for the charity to mine tokens that we create that has a value tied to the USD. Donors will then create accounts in which they will purchase Ethereum to then purchse the mined tokens as a donation to the charity. The charity wallet will then collect these donated tokens and pass them to in-country partners who will distribute the mined tokens to the final recipient of the donations. We will also create a front end Streamlit model that will mimic a phone app to be created for use by the final recipient.
---
* [X] Step 1: Create wallet for charity which will mine the tokens based on the USD and be the main wallet for the project.
* [] Step 2: Create wallet accounts for the donors who will purchase Ethereum into their wallet to then purchase the mined coins from the main charity.
* [X] Step 3: Main charity wallet will then pass the donated USD based coins that were mined and purchsed to the in-country partners’ wallets.
* [X] Step 4: Create wallet for the in-country partner to receive the coins from the charity to pass to the individual.
* [X] Step 5: Create wallets for the individuals who will be receiving the final donation to be able to accept and use the tokens.
* [X] Step 6: Create wallet for the vendor where the individual will be using coins to purchase goods and then that the vendor can trade back into the charity.
* [] Step 7: Create a frontend model that will mimic an app for the interaction of the final individual with their account
---
## Powerpoint
PowerPoint from the final presentation

---
## Analysis
* Failed to create a coin based on the USDC.
* Was not able to create a frontend model for the interaction of the individul account due to time constraint
* Using Solidity 0.8.4 we didn’t need to worry about Safe Math
* Was able to create a prototype for moving coin from donor to charity.
* Created a prototype system of moving coins throughout the charity, in-country partner, individual, vendor and back to the charity.
* Created a burn function to keep the amounts of coins in the contracts stable per the dollar value in the contracts.
---
## Next Steps
* Find a way to create the coin build based on a stable coin like the USDC.
* Adjust portions of the contract to have more pass-through capability.
* Rewrite contracts to make exchanging coins a more seamless transaction.
* Find ways to streamline to minimize gas charges.
* Test for security.
* Deploy / Test…….Deploy / Test………Deploy / Test
* Implement a card that would have the individuals account information to use at the vendors.
* Automate donor functions to be usable with a QR code or similar technology

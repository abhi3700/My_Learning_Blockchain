# Merkle Airdrop

## Background
* The idea of token Air Drops is interesting and a powerful way to quickly get tokens into the hands of a large customer base, but the current incarnations are more closely related to carpet bombing than to air-dropping.
* With airdrops , the number of people who register to receive tokens depending on their size can range from hundreds, thousands or even tens of thousands of people.
* Ethereum ‘s storage fees as well as transaction fees are currently not cheap at all, imagine an array of contracts containing thousands of registered addresses will be very expensive, not to mention new transactions. address to the array again. In general, the above Airdrop contract design solution is not at all optimal for your wallet.
* The Token airdrops has the following demerits:
	- __Account disturbance__: Accounts are littered with fragments of token shrapnel whether they wanted them or not, and in many cases, whether the account can even spend them.
	- __High fees__: the ether gobbled up in fees and lost utility due to network congestion from the seeding transactions.
	- __Storage__: contract storage for token balances that cannot be used.
	- __Too many transactions__: oodles of transactions required to disseminate tokens.
* So, there is a friendlier way to scatter tokens with a wide distribution using __redeem-based Merkle Air Drops__.
	- With Merkle Airdrop , we will not have to worry about having to save a large number of addresses registered in the contract, while still ensuring the verification of the claim address registered before or not? From there, it saves a lot of costs in Airdrop .
	- Deploy of any number of tokens in a single, cheap fixed-cost transaction.
	- The __receiver pays the `gas`__; which provides a bound on spam and dust as most people won’t pay a 12 cent transaction fee for 10 cents worth of tokens.
	- All token holders have access to claim and use their tokens __immediately__ and do not need to wait for seed transactions
	- Lost private keys and contracts without `approve` proxy methods __do not__ waste blockchain state size with un-spendable balances or seeding transactions and do not waste ether
	- Tokens are often only needed on-chain in specific circumstances, such as transferring; hodlers can __keep them off-chain__ (or at the very least move them on-chain during dips in gas prices).
	- People __aren’t spooked__ by mysterious tokens showing up in their accounts (although this is likely the PR play that tokens were actually going)

> technically, anyone may pay the gas, likely this would be the recipient of the tokens, but this also opens interesting use cases to explore; perhaps priority members get their token allocation paid by the token issuer, for example

* Objectives
	- to increase the number of token holders
	- to broaden the promotion for the upcoming token. 

## Procedure
### Summary
1. Of course, you must deploy the ERC-20 contract token first.
1. Writing Airdrop contract: Contract saves a list of addresses that register to receive tokens. After the Airdrop registration period ends , users can call the contract to claim token.
1. In addition, we can build more bots (such as Telegram bot) to track users with the condition follow page, share articles. v..v to register for Airdrop.

### Comprehensive
1. Owner of contract prepares a list of addresses with many entries and publishes this list in public static `.js` file in `JSON` format
1. Owner reads this list, builds the __merkle tree structure__ and writes down the __Merkle root__ of it.
1. Owner creates contract and places __calculated Merkle root__ into it.
1. Owner says to users, that they can claim their tokens, if they owe any of addresses, presented in list, published on onwer's site.
1. User wants to claim his N tokens, he also builds Merkle tree from public list and prepares Merkle proof, consisting from log2N hashes, describing the way to reach Merkle root
1. User sends transaction with Merkle proof to contract
1. Contract checks Merkle proof, and, if proof is correct, then sender's address is in list of allowed addresses, and contract does some action for this use. In our case it mints some amount of token

## Merkle Tree


## Smart Contract


## References
* [YouTube | Bitcoin 101 - Merkle Roots and Merkle Trees - Bitcoin Coding and Software - The Block Header](https://www.youtube.com/watch?v=gUwXCt1qkBU)
* [YouTube | How Merkle Trees Enable the Decentralized Web!](https://www.youtube.com/watch?v=YIc6MNfv5iQ)
* [Uniswap Distributor Code](https://etherscan.io/address/0x090d4613473dee047c3f2706764f49e0821d256e#code)
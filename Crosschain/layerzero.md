# LayerZero

## Overview

- **Founders**: Bryan, Ryan, and Caleb
- It's considered as "**the language of blockchains**".
- It's often compared to **TCP/IP of internet**.
- It is a protocol that allows blockchains to communicate with each other.

## Notes

- v1 vs v2:
  - In v1, verification and execution were provided by Oracles and Relayers. In v2, they’re provided by **Decentralized Verifier Networks (DVNs)** and **Executors**.
  - What hasn’t changed between v1 and v2 is that endpoints are immutable and validation libraries are append-only.
  - Importantly, in v2, LayerZero Labs has totally decoupled security from execution in order to guarantee censorship-resistance without impacting liveness, or the ability of the protocol to continue functioning and processing transactions without interruption.

- Traditional way of **bridging chains**:
  
  So if you wanted to send your tokens from say, Ethereum to Polygon, in order to use an app on Polygon, you’d go to a bridge and the bridge would do a few things:

  - **Lock the Original Asset**. Essentially, the bridge sends your ETH to a smart contract that holds it “securely.”

  - **Create a Wrapped Version**. The bridge issues a “wrapped” version of your ETH, WETH, that represents your original ETH but works with Polygon’s rules.

  - **Give You the Wrapped Version**. The bridge puts the WETH in your wallet on Polygon, which you can use to do things on Polygon.

  - **Redeem the Original Asset**. To redeem your original ETH on Ethereum, you send your WETH back to the bridge, the bridge burns it, unlocks your original ETH, and puts it in your Ethereum wallet, where you can use it to do things on Ethereum.

- Bridges hacks: All of that locked ETH (or whatever locked token) is a gigantic flashing sign that there’s a pot of money hackers can try to break into
  - [Wormhole Bridge between Solana and Ethereum for $326 million](https://cointelegraph.com/news/wormhole-token-bridge-loses-321m-in-largest-hack-so-far-in-2022) on Feb 22.
  - [Ronin Bridge between Ronin and Ethereum for $624 million](https://www.coindesk.com/tech/2022/03/29/axie-infinitys-ronin-network-suffers-625m-exploit/) on Mar 22.
  
  There was another problem that is lack of nodes that guarantee the security of money pots (locked tokens). Ronin was attacked that way. It was way too centralized with few nodes getting compromised via sending phishing clicks by one of the nodes & then 2/3 of the nodes were compromised.

  <details><summary>More hacks:</summary>

  ![](../img/crosschain_bridge_hacks.png)

  </details>

  Second, **they’re slow, painful, and a little bit scary**. Bridging tokens means figuring out how to get the native token of the chain you’re bridging to in order to pay gas fees for that end of the transaction, putting your valuable tokens into a website, signing them away, and then waiting for a painfully long time. More than once, I’ve worried if my tokens were lost forever while I waited.

## References

- [LayerZero: The Language of the Omnichain](https://www.notboring.co/p/layerzero-the-language-of-the-omnnichain)

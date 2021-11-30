# Laser supplier info analysis and selection of best suppliers

This is the second part of the project, connected with laser suppliers (the first one - https://github.com/jularina/LaserSupplier1).

That project provides tool for laser supplier selection decision making, based on collected info.
The discrete Bayesian Network and propagation algorithm are used for multiple-criteria decision-making (MCDM).

The process of data retrieving from database MongoDB Atlas and analysis is shown on Pic.1.

![Pic.2](https://user-images.githubusercontent.com/56595596/144019476-51e4731d-a181-43de-b994-2e419aa4916d.png)

Files through which information is requested from the database are processed and included in the network:

bayes_network – a file with a prescribed structure of a Bayesian network, gives a vendor estimate.

pipelines – file with requests from the database.

params_bayes – the file of the connection between the estimates for the suppliers calculated from the base and the network.

The structure of the bayesian network is shown on Pic.2.

![Pic.2](https://user-images.githubusercontent.com/56595596/144019942-31537919-df3a-410b-9532-d4713a542304.png)

The process goes from top to down node, which form the overall values of each laser supplier. The posterior distrivutions for nodes are formed with pairwise comparison method. Prior probabilities are calculated from info in MongoDB database.




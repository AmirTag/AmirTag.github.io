---
layout: page
title: Research
permalink: /research/
---

### Optimal Transportation methods in nonlinear filtering:       {#FPF}
<p align="center">
<img src="../images/FPF-artwork-with-Poisson.png" width="440"/>
</p>

Uncertainty is, more than ever, an integral part of modern control system applications. We use models that are learned from data, fuse variety of noisy sensors, and augment machine learning modules that are inherently stochastic. Nonlinear filtering is a principled approach to quantify uncertainty and as- similate noisy sensory data in a probabilistic framework. However, existing nonlinear filtering algorithms face critical limitations due to (i) highly nonlinear and complex models (ii) curse of dimensionality; (ii) and incorrect specification of models and noise statistics. This research project is aimed at overcoming these limitations.

- [Optimal Transportation Methods in Nonlinear Filtering: The feedback particle filter](https://ieeexplore.ieee.org/document/9491060)([arXiv](https://arxiv.org/abs/2102.10712))     

- [An Optimal Transport Formulation of Bayes' Law for Nonlinear Filtering Algorithms](https://arxiv.org/abs/2203.11869)

- [An optimal transport formulation of the ensemble Kalman filter](https://doi.org/10.1109/TAC.2020.3015410) ([arXiv](https://arxiv.org/abs/1910.02338))        





----------
### Interplay between optimization and sampling:   {#SM}
<p align="center">
<img src="../images/sampling-optimization.png" width="350"/>
<img src="../files/mnist-traj.png" width="300"/>
</p>

Optimization and sampling algorithms share remarkable similarities in general, as highlighted by the similarity between stochastic gradient descent and Langevin sampling. In fact, sampling can be viewed as an optimization problem on the space of probability distributions. The goal of this research is to bridge the gap between optimization and sampling by employing optimization algorithms specifically for the purpose of sampling, using the Riemannian geometry, as provided by optimal mass transport. 

- [Variational Wasserstein gradient flow](https://arxiv.org/abs/2112.02424)  
    
- [Accelerated flow for probability distributions](http://proceedings.mlr.press/v97/taghvaei19a.html) ([arXiv](https://arxiv.org/abs/1901.03317))        



----------
### Computational methodology for optimal mass transportation:      {#OT}
<p align="center">
<img src="../images/OT-drawing.png" width="350"/>
</p>

There is a growing interest in application of the optimal transportation theory in machine learning and control related problems. The main reason is that the optimal transportation theory provides powerful and elegant geometrical tools to view and manipulate probability distributions. The objective of this  ressearch is to develop efficient data-driven computational algorithms that provide reliable approximations to these geometrical tools in high dimensions.


- [Scalable computations of Wasserstein barycenter via input convex neural networks](https://arxiv.org/abs/2007.04462)  


- [Optimal transport mapping via input-convex neural networks](http://proceedings.mlr.press/v119/makkuva20a.html) ([arXiv](https://arxiv.org/abs/1908.10962))              


----------
### Fundamental limitations in stochastic thermodynamics:  {#Thermo}
<p align="center">
<img src="../files/engine.jpg" width="400"/>
</p>

Classical thermodynamics is inherently static and can not capture non-equilibrium transitions and the power that can be extracted from an engine in finite time.
To this end, the framework of stochastic thermodynamics was developed in recent years to allow quantifying thermodynamic quantities in finite time transitions. The objective of this project is to study fundamental limits in dissipation and in power generation by thermodynamic processes. Remarkabley, these problems can be viewed as optimal control problems for probabibility distributions where optimal mass transport plays a central role.

- [Energy harvesting from anisotropic fluctuations](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.104.044101)([arXiv](https://arxiv.org/abs/2108.00334))        
   
- [On the relation between information and power in stochastic thermodynamic engines](https://ieeexplore.ieee.org/document/9426929)([arXiv](https://arxiv.org/abs/2103.03986)) 

- [Maximal power output of a stochastic thermodynamic engine](https://doi.org/10.1016/j.automatica.2020.109366) ([arXiv ](https://arxiv.org/abs/2001.00979))  

<!--
---
layout: page
title: Publications
permalink: /publications/
---
#### Preprints/Under review:
- [A lasso-alternative to Dijkstra's algorithm for identifying short paths in networks]()        
Anqi Dong, Amirhossein Taghvaei, Tryphon T. Georgiou        



- [Stochastic thermodynamic engines under time-varying temperature profile](https://arxiv.org/abs/2207.05069)       
Rui Fu, Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou


- [Minimal entropy production in the presence of anisotropic temperature fields](https://arxiv.org/abs/2302.04401)      
Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou      
   


#### Journal publications:
- [A Matching Principle for Power Transfer in Stochastic Thermodynamics](https://ieeexplore.ieee.org/document/10149098) ([arXiv](https://arxiv.org/abs/2210.01062))     
IEEE Control Systems Letters, vol. 7, pp. 2107-2112, 2023       
Olga Movilla Miangolarra, Amirhossein Taghvaei, Tryphon T. Georgiou            
 


- [A Survey of Feedback Particle Filter and related Controlled Interacting Particle Systems (CIPS)](https://www.sciencedirect.com/science/article/abs/pii/S136757882300010X)([arXiv](https://arxiv.org/abs/2301.00935))  Annual Reviews in Control, Volume 55, 2023, Pages 356-378.       
Amirhossein Taghvaei, Prashant G. Mehta.          


- [An optimal control approach to particle filtering](https://www.sciencedirect.com/science/article/abs/pii/S0005109823000444) ([arXiv](https://arxiv.org/abs/2110.03199))           
Automatica, Volume 151, 2023, 110894.       
Qinsheng Zhang, Amirhossein Taghvaei, Yongxin Chen  

- [Inertialess Gyrating Engines](https://academic.oup.com/pnasnexus/article/1/5/pgac251/6798386) ([arXiv](https://arxiv.org/abs/2208.01292))   
PNAS Nexus, Volume 1, Issue 5, November 2022      
Jordi V. Siches, Olga M. Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou    

- [Controlled Interacting Particle Algorithms for Simulation-based Reinforcement Learning](https://www.sciencedirect.com/science/article/abs/pii/S0167691122001694) ([arXiv](https://arxiv.org/abs/2107.01244))      
Systems & Control Letters, Volume 170, 2022       
Anant Joshi, Amirhossein Taghvaei, Prashant G. Mehta, Sean P. Meyn  

- [Geometry of finite-time thermodynamic cycles with anisotropic thermal fluctuations](https://ieeexplore.ieee.org/document/9802668) ([arXiv](https://arxiv.org/abs/2203.12483))         
IEEE Control Systems Letters, vol. 6, pp. 3409-3414, 2022      
Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou 

- [Thernodynamic engine powered by anisotropic fluctuations](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.023218) ([arXiv](https://arxiv.org/abs/2203.07573))          
Phys. Rev. Research, 4, 023218, Jun 2022      
Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou  


- [Energy harvesting from anisotropic fluctuations](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.104.044101) ([arXiv](https://arxiv.org/abs/2108.00334))        
Phys. Rev. E 104, 044101, Oct 2021      
Olga Movilla Miangolarra, Amirhossein Taghvaei, Rui Fu, Yongxin Chen, Tryphon T. Georgiou 

- [Optimal Transportation Methods in Nonlinear Filtering: The feedback particle filter](https://ieeexplore.ieee.org/document/9491060) ([arXiv](https://arxiv.org/abs/2102.10712))                 
IEEE Control Systems Magazine (CSM), vol. 41, no. 4, pp. 34-49, Aug. 2021                       
Amirhossein Taghvaei and Prashant G. Mehta  


- [On the Lyapunov Foster criterion and Poincare inequality for Reversible Markov Chains](https://ieeexplore.ieee.org/document/9456997)) ([arXiv](https://arxiv.org/abs/2005.08145))    
Transactions of Automatic Control (TAC), vol. 41, no. 5, pp. 2605-2609, 2021    
Amirhossein Taghvaei and Prashant G. Mehta     


- [Underdamped stochastic thermodynamic engines in contact with a heat bath with arbitrary temperature profile](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.103.062103) ([arXiv](https://arxiv.org/abs/2101.05396)) Phys. Rev. E 103, 062103, June 2021   
Olga Movilla Miangolarra, Rui Fu, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou 


- [On the relation between information and power in stochastic thermodynamic engines](https://ieeexplore.ieee.org/document/9426929) ([arXiv](https://arxiv.org/abs/2103.03986))      
IEEE Control Systems Letters (L-CSS), vol. 6, pp. 434-439, 2022     
Amirhossein Taghvaei, Olga Movilla Miangolarra, Rui Fu, Yongxin Chen, Tryphon T. Georgiou     


- [Feedback particle filter for collective inference](https://www.aimsciences.org/article/doi/10.3934/fods.2021018) ([arXiv](https://arxiv.org/abs/2010.06655))                   
Foundations of Data Science (FoDS) on Data Assimilation, 3(3), 543:561, 2021     
Jin Won Kim, Amirhossein Taghvaei, Yongxin Chen, Prashant G. Mehta

- [Maximal power output of a stochastic thermodynamic engine](https://doi.org/10.1016/j.automatica.2020.109366) ([arXiv ](https://arxiv.org/abs/2001.00979))   
Automatica, 123:109366, 2021         
Rui Fu, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou    


- [An optimal transport formulation of the ensemble Kalman filter](https://doi.org/10.1109/TAC.2020.3015410) ([arXiv](https://arxiv.org/abs/1910.02338))        
Transactions of Automatic Control (TAC), vol. 66, no. 7, pp. 3052-3067, July 2021     
Amirhossein Taghvaei and Prashant G. Mehta    

- [Fractional SIR Epidemiological Models](https://doi.org/10.1038/s41598-020-77849-7)    
Scientefic Reports, 10(1):20882, 2020         
Amirhossein Taghvaei, Tryphon T. Georgiou, Larry Norton, Allen R. Tannenbaum 

- [Diffusion map-based algorithm for gain function approximation in the feedback particle filter](https://doi.org/10.1137/19M124513X) ([arXiv](https://arxiv.org/abs/1902.07263)) SIAM/ASA Journal on Uncertainty Quantification, 8(3):1090–1117, 2020
Amirhossein Taghvaei, Prashant G. Mehta, Sean P. Meyn    
 

- [A mean-field optimal control formulation for global optimization](https://doi.org/10.1109/TAC.2018.2833060) ([arXiv](https://arxiv.org/abs/1701.02413))       
IEEE Transactions on Automatic Control (TAC), 64, no. 1, pp. 282-289, Jan. 2019  
Chi Zhang, Amirhossein Taghvaei, Prashant G. Mehta    


- [Kalman filter and its modern extensions for the continuous-time nonlinear filtering problem](https://doi.org/10.1115/1.4037780) ([arXiv](https://arxiv.org/abs/1702.07241))   
Journal of Dynamic Systems, Measurement, and Control, 140(3):030904, 2018          
Amirhossein Taghvaei, Jana de Wiljes, Prashant G. Mehta, and Sebastian Reich     


- [Feedback Particle Filter on Riemannian Manifolds and Matrix Lie groups](https://doi.org/10.1109/TAC.2017.2771336) ([arXiv](https://arxiv.org/abs/1701.02416))       
IEEE Transactions on Automatic Control (TAC), 63(8):2465–2480, 2018           
Chi Zhang, Amirhossein Taghvaei, Prashant G. Mehta    


#### Machine Learning Conferences:
- [Variational Wasserstein gradient flow](https://proceedings.mlr.press/v162/fan22d.html) ([arXiv](https://arxiv.org/abs/2112.02424))  
International Conference of Machine Learning (ICML), PMLR 162:6185-6215, 2022
Jiaojiao Fan, Qinsheng Zhang, Amirhossein Taghvaei, Yongxin Chen 

- [Scalable computations of Wasserstein barycenter via input convex neural networks](https://proceedings.mlr.press/v139/fan21d) ([arXiv](https://arxiv.org/abs/2007.04462))  
International Conference of Machine Learning (ICML), PMLR 139:1571-1581, 2021
Jiaojiao Fan, Amirhossein Taghvaei, Yongxin Chen   


- [Optimal transport mapping via input-convex neural networks](http://proceedings.mlr.press/v119/makkuva20a.html) ([arXiv](https://arxiv.org/abs/1908.10962))              
International Conference on Machine Learning (ICML), PMLR 119:6672-6681, 2020         
Ashok Makkuva, Amirhossein Taghvaei, Sewoong Oh, Jason Lee    
 

- [Accelerated flow for probability distributions](http://proceedings.mlr.press/v97/taghvaei19a.html) ([arXiv](https://arxiv.org/abs/1901.03317))        
International Conference on Machine Learning (ICML), PMLR 97:6076-6085, 2019          
Amirhossein Taghvaei, Prashant G. Mehta      


- [How regularization affects the critical points in linear neural networks](https://papers.nips.cc/paper/6844-how-regularization-affects-the-critical-points-in-linear-networks) ([arXiv](https://arxiv.org/abs/1709.09625))         
Advances in Neural Information Processing Systems (NeurIPS), 2502–2512, Long Beach, December 2017           
Amirhossein Taghvaei, Jin W. Kim, Prasshant G. Mehta       


#### Control Conferences:
- [Optimal Transport Particle Filters](https://arxiv.org/abs/2304.00392)                         
IEEE Conference on Decision and Control (CDC), Singapore, 2023 (accepted)         
Mohammad Al-Jarrah, Amirhossein Taghvaei, Bamdad Hosseini           


- [A Matching Principle for Power Transfer in Stochastic Thermodynamics](https://arxiv.org/abs/2210.01062)                     
IEEE Conference on Decision and Control (CDC), Singapore, 2023 (accepted)        
Olga Movilla Miangolarra, Amirhossein Taghvaei, Tryphon T. Georgiou      


- [Duality-Based Stochastic Policy Optimization for Estimation with Unknown Noise Covariances](https://ieeexplore.ieee.org/document/10155989) ([arXiv](https://arxiv.org/abs/2210.14878)) IEEE American Control Conference (ACC), San Diego, 2023          
Shahriar Talebi, Amirhossein Taghvaei, Mehran Mesbahi.   


- [Minimal entropy production in anisotropic temperature fields](https://ieeexplore.ieee.org/document/10156443) ([arXiv](https://arxiv.org/abs/2210.01062))        
IEEE American Control Conference (ACC), San Diego, 2023  
Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou      


- [An Optimal Transport Formulation of Bayes' Law for Nonlinear Filtering Algorithms](https://ieeexplore.ieee.org/document/9992776) ([arXiv](https://arxiv.org/abs/2203.11869))          
IEEE Conference on Decision and Control (CDC), Cancun, Mexico, 2022        
Amirhossein Taghvaei, Bamdad Hosseini     


- [Geometry of finite-time thermodynamic cycles with anisotropic thermal fluctuations](https://ieeexplore.ieee.org/document/9802668)([arXiv](https://arxiv.org/abs/2203.12483))         
IEEE Conference on Decision and Control (CDC), Cancun, Mexico, 2022        
Olga Movilla Miangolarra, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou       


- [Optimality vs Stability Trade-off in Ensemble Kalman Filters](https://www.sciencedirect.com/science/article/pii/S2405896322027082)([arXiv](https://arxiv.org/abs/2010.09920))        
25th International Symposium on Mathematical Theory of Networks and Systems (MTNS 2022), Bayreuth, Germany, 2022                
Amirhossein Taghvaei, Prashant G. Mehta, Tryphon T. Georgiou           


- [On the relation between information and power in stochastic thermodynamic engines](https://ieeexplore.ieee.org/document/9426929)([arXiv](https://arxiv.org/abs/2103.03986))      
IEEE Conference on Decision and Control (CDC), Austin, December 2021          
Amirhossein Taghvaei, Olga Movilla Miangolarra, Rui Fu, Yongxin Chen, Tryphon T. Georgiou     


- [Lasso formulation of the shortest path problem](https://ieeexplore.ieee.org/document/9303909) ([arXiv](https://arxiv.org/abs/2005.09152))                 
IEEE Conference on Decision and Control (CDC), 402-407, Jeju Island, Republic of Korea, December 2020         
Anqi Dong, Amirhossein Taghvaei, Tryphon T. Georgiou       

- [Harvesting energy from a periodic heat bath](https://ieeexplore.ieee.org/document/9304271) ([arXiv](https://arxiv.org/abs/2101.02239))           
IEEE Conference on Decision and Control (CDC), 3034-3039, Jeju Island, Republic of Korea, December 2020        
Rui Fu, Olga Movilla, Amirhossein Taghvaei, Yongxin Chen, Tryphon T. Georgiou       

- [Deep FPF: Gain function approximation in high-dimensions](https://ieeexplore.ieee.org/document/9304260) ([arXiv](https://arxiv.org/abs/2010.01183))          
IEEE Conference on Decision and Control (CDC), 4790-4795, Jeju Island, Republic of Korea, December 2020        
S. Yagiz Olmez, Amirhossein Taghvaei, Prashant G. Mehta   

- [Bio-inspired Learning of Sensorimotor Control for Locomotion](https://ieeexplore.ieee.org/document/9147889) ([arXiv](https://arxiv.org/abs/1910.02556))           
IEEE American Control Conference (ACC), 2188–2193, Denver, July 2020      
Tixian Wang, Amirhossein Taghvaei, Prashant G. Mehta       


- [Q-learning for POMDP: An application to learning locomotion gaits](https://ieeexplore.ieee.org/document/9030143) ([arXiv](https://arxiv.org/abs/1910.00107))            
IEEE Conference on Decision and Control (CDC), 2758–2763, Nice, France, December 2019       
Tixian Wang, Amirhossein Taghvaei, Prashant G. Mehta        


- [An approach to duality in nonlinear filtering](https://ieeexplore.ieee.org/document/8815136) ([arXiv](https://arxiv.org/abs/1809.10762))            
IEEE American Control Conference (ACC), 5360–5365, Philadelphia, July 2019      
Jin W. Kim, Amirhossein Taghvaei, Prashant G. Mehta, Sean P. Meyn        
     
- [Error analysis of the stochastic linear feedback particle filter](https://ieeexplore.ieee.org/document/8619806) ([arXiv](https://arxiv.org/abs/1809.07892))            
IEEE Conference on Decision and Control (CDC), 7194–7199, Miami, December 2018             
Amirhossein Taghvaei, Prashant G. Mehta 

- [Derivation and Extensions of the Linear Feedback Particle Filter based on Duality Formalisms](https://ieeexplore.ieee.org/document/8618878) ([arXiv](https://arxiv.org/abs/1804.04199))               
IEEE Conference on Decision and Control (CDC), 7188–7193, Miami, December 2018           
Jin W. Kim, Amirhossein Taghvaei, Prashant G. Mehta      

- [Error analysis of the linear feedback article filter](https://ieeexplore.ieee.org/document/8430867) ([arXiv](https://arxiv.org/abs/1710.11008))      
IEEE American Control Conference (ACC), 4261–4266, Milwaukee, June 2018          
Amirhossein Taghvaei, Prashant G. Mehta      

- [Error Estimates for the Kernel Gain Function Approximation in the Feedback Particle Filter](https://ieeexplore.ieee.org/document/7963661) ([arXiv](https://arxiv.org/abs/1612.05606))       
IEEE American Control Conference (ACC), 4576–4582, Seattle, May 2017          
Amirhossein Taghvaei, Prashant G. Mehta. S. P. Meyn           

- [Attitude Estimation of a Wearable Motion Sensor](https://ieeexplore.ieee.org/document/7963660)       
IEEE American Control Conference (ACC), 4570–4575, Seattle, May 2017       
Chi Zhang, Amirhossein Taghvaei, Prashant G. Mehta      
    
- [Gain Function Approximation in the Feedback Particle Filter](https://ieeexplore.ieee.org/document/7799105) ([arXiv](https://arxiv.org/abs/1603.05496))     
IEEE Conference on Decision and Control (CDC), 5446–5452 Las Vegas, December 2016        
Amirhossein Taghvaei, Prashant G. Mehta     
 
- [Attitude Estimation with Feedback Particle Filter](https://ieeexplore.ieee.org/document/7799104)      
IEEE Conference on Decision and Control (CDC), 5440–5445, Las Vegas, December 2016        
Chi Zhang, Amirhossein Taghvaei, Prashant G. Mehta       

- [An Optimal Transport Formulation of Linear Feedback Particle Filter](https://ieeexplore.ieee.org/abstract/document/7525474) ([arXiv](https://arxiv.org/abs/1510.01948))        
IEEE American Control Conference (ACC), 3614–3619, Boston, June 2016        
Amirhossein Taghvaei, Prashant G. Mehta       
 
- [Feedback Particle Filter on Matrix Lie group](https://ieeexplore.ieee.org/document/7525330)        
IEEE American Control Conference (ACC), 2723–2728, Boston, June 2016         
Chi Zhang, Amirhossein Taghvaei, Prashant G. Mehta        
 
- [A Coupled Oscillator-based Control Architecture for Locomotory Gaits](https://ieeexplore.ieee.org/abstract/document/7039930)        
IEEE Conference on Decision and Control (CDC), 3487–3492, Los Angeles, December 2014       
Amirhossein Taghvaei, Seth A. Hutchinson, and Prashant G. Mehta       


#### Thesis:

- [Design and analysis of particle-based algorithms for nonlinear filtering and sampling](http://hdl.handle.net/2142/105673)    
Ph.D. Dissertation, University of Illinois at Urbana-Champaign, 2019           
Amirhossein Taghvaei        

---
layout: page
title: Mentorship
permalink: /mentorship/
---
### Ph.D. students (current)

- Mohammad Al-Jarrah, University of Washington, Seattle
- Olga Movilla, University of California, Irvine
- Anqi Dong, University of California, Irvine

### Master's students (current)
-  Hasan Horata, University of Washington, Seattle     
-  Siri Gadipudi, University of Washington, Seattle.   


--------

### Master's students (former)
- Tixian Wang, University of Illinois at Urbana-Champaign

- Yagiz Olmez, University of Illinois at Urbana-Champaign  

--------
### Undergraduates (former)
- Ayano Hiraka, Kumar Gandhi, Peter Ivanov, Ulzee An, University of Illinois at Urbana-Champaign  

-->
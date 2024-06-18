# Overview

The purpose of this exercise is to build a multi-agent system that can take a description of a clients legal problem and produce a "legally defensible & appropriate" pre-action letter that a solicitor can tweak and then sign off on.

The definition of "legally defensible & appropriate" is somewhat subjective (and intentionally vague!), but the general criteria is:

1. The letter should cite only relevant England & Wales legislation
2. The letter must not "hallucinate" any legal concepts, terminology, references.
3. The letter must be constructed in such a way that it would be recognised as constituting a stage of the pre-action process
4. The letter must use British English

# Problem Description

The client provides the following information:

My name is John Johnson I seek a lawyer to draft a preaction to a neighbour. I'm the landlord of the property (which is 4 Springer Close, Birmingham BH4 1PL) and have tenants in situ. My wife and I own the property and have experienced the very same intimidation at first hand from the neighbours in question. We have rented out the property over the last three years and now the harassment has extended to our tenants. Our tenants, a professional couple who are of a gentle and non-confrontational nature are highly anxious and wish to cut short their tenancy if this continues. We wish to make clear to the neighbours in writing that they must stop in their threatening behaviour and that in the event of our tenants having to forcibly exit the property we will make a direct claim on them for all damages and loss of earnings. We consulted with our lettings agent (Keithly Estate Agents in Birmingham) and they agree this is the right approach to take in going forwards. The neighbours consistently make loud noises at night and they have a large dog that they let roam their adjacent garden. The neighbours address is 7 Springer Close, Birmingham BH4 1PL
